#include<iostream>
using namespace std;
/* Time */

class Time
{
	int h,m;
public:
	Time(){ h=0;m=0; }
	Time(int H,int M){ h=H; m=M; }
	void add(int min);
	int cmp(Time &t);
	void setTime(char *str);
	void setTime(Time t){h=t.getHour(); m=t.getMinute();}
	void display(){ cout<<h<<":"<<m; }
	void setHour(int H){ h=H; }
	void setMinute(int M){ m=M; }
	int getHour(){ return h; }
	int getMinute(){ return m; }
};
void Time::add(int min)
{
	if(min >= 60)
	{
		h+=min/60;
		min%=60;
	}
	m+=min;
	h+=m/60;
	m%=60;
}
int Time::cmp(Time &t)
{
	if(t.getHour() - h != 0)
		return t.getHour()-h;
	else
		return t.getMinute()-m;
}
void Time::setTime(char *str)
{
	h=atoi(str);
	int i=0;
	while(str[i] != ':')str++;
	str++;
	m=atoi(str);
}


void swap(Time  &t1,Time &t2)
{
	Time temp(t1);
	t1.setTime(t2);
	t2.setTime(temp);
}
int timeCmp(Time &t1,Time &t2)
{
	return t2.cmp(t1);
}

/* MinPriorityQueue */
class MinPriorityQueue
{
	Time *timeList;
	int length;
	int N;
private:	
	void minHeapify(int i);
	int parent(int i){ i=i+(i&1); return (i>>1)-1; }
	void decreaseTime(int i,Time);
	int isPowerOf2(int x);
public:
	MinPriorityQueue(int);
	~MinPriorityQueue();
	Time min(){ return timeList[0]; }
	Time extractMin();
	void insert(Time t);
	void display(); 
	bool empty();
};
/* Public functions */
MinPriorityQueue::MinPriorityQueue(int size)
{
	length=size;
	timeList=new Time[size];
	N=0;
}
MinPriorityQueue::~MinPriorityQueue()
{
	int N=0;
	int length=0;
	delete[] timeList;
}
Time MinPriorityQueue::extractMin()
{
	if(N <= 0)
	{
		Time temp;
		temp.setTime("99:99");
		return temp; /* error */
	} 
	Time min(timeList[0]);
	timeList[0]=timeList[--N];
	minHeapify(0);
	return min;
}
void MinPriorityQueue::insert(Time t)
{
	timeList[N++].setTime("99:99");
	decreaseTime(N-1,t);
}
void MinPriorityQueue::display()
{
	int i=0;
	while(i < N)
	{
		if(isPowerOf2(i+1) != -1)
			cout<<endl;
		timeList[i].display();
		cout<<"  ";
		i++;
	}	
}
bool MinPriorityQueue::empty()
{
	return (N <= 0)?true:false;
}
/* Private Functions */
void MinPriorityQueue::decreaseTime(int i,Time newTime)
{
	if(timeCmp(newTime,timeList[i]) > 0)
		return;
	timeList[i].setTime(newTime);
	while(parent(i) >= 0 && timeCmp(timeList[i],timeList[parent(i)]) < 0)
	{
		swap(timeList[i],timeList[parent(i)]);
		i=parent(i);
	}
}

void MinPriorityQueue::minHeapify(int i)
{
	while((i<<1)+2 < N)
	{
		int k=(timeCmp(timeList[(i<<1)+1], timeList[(i<<1)+2]) < 0 )? (i<<1)+1:(i<<1)+2;
		if(timeCmp(timeList[k],timeList[i]) > 0)
			return;
		swap(timeList[k],timeList[i]);
		i=k;
	}		
	/* if node i has only one child */
	if((i<<1)+1 < N)
	 if(timeCmp(timeList[i],timeList[(i<<1)+1]) > 0)
		swap(timeList[i],timeList[(i<<1)+1]);
}
int MinPriorityQueue::isPowerOf2(int x) 
{
	if(!x) return -1;
	int count=0;
	while((x&1) == 0)
	{
		count++;
		x>>=1;
	}	
	if(x>>1) return -1;
	return count;
}

void getNo(int &a)
{
	char str[10];
	cin.getline(str,8);
	a=atoi(str);
}
void get2Nos(int &a,int &b)
{
  char str[10];
  cin.getline(str,8);
  char *pch;
  pch = strtok (str," ");
  a=atoi(pch);
  pch = strtok (NULL," ");
  b=atoi(pch);
}

void get2Times(Time &t1,Time &t2)
{
  char str[20];
  cin.getline(str,12);
  char *pch;
  pch = strtok(str," ");
  t1.setTime(pch);
  pch = strtok (NULL," ");
  t2.setTime(pch);
}
int noTrains(MinPriorityQueue &timeTable, MinPriorityQueue &extra)
{
	int countA=0;
	Time tt,te;
	while(timeTable.empty() != true)
	{
		tt=timeTable.extractMin();
		if(extra.empty())
			countA++;
		else
		{
			te.setTime(extra.min());
			if(timeCmp(tt,te) < 0)
		 		countA++;
			else
		 		extra.extractMin();	
		}
	}
	return countA;
}
		
void runTestCase(int &countA,int &countB)
{
	int T,NA,NB;
	getNo(T);
	get2Nos(NA,NB);
	Time t1,t2;
	MinPriorityQueue timeTableA(200),timeTableB(200),extraA(200),extraB(200);
	for(int i=1;i <= NA;i++)
	{
		get2Times(t1,t2);
		timeTableA.insert(t1);
		t2.add(T);
		extraB.insert(t2);
	}
	for(int i=1;i <= NB;i++)
	{
		get2Times(t1,t2);
		timeTableB.insert(t1);
		t2.add(T);
		extraA.insert(t2);
	}
	countA=noTrains(timeTableA,extraA);
	countB=noTrains(timeTableB,extraB);
}
int main()
{
	int N,countA,countB;
	getNo(N);
	for(int i=1;i <= N;i++)
	{
		runTestCase(countA,countB);
		cout<<"Case #"<<i<<": "<<countA<<" "<<countB<<endl;
	}
	return 0;
}
