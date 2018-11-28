#include<iostream>
#include<fstream>
using namespace std;
//>>,+,=,>,<=
class Time
{
    private:
        int hour,minute;
    public:
        Time();
        Time(Time&);
        Time(int,int);
        void setTime(int,int);
        void format();
        void input(istream&);
		void operator+(Time);
		void operator=(Time);
		bool operator<(Time);
		bool operator>(Time);
	friend Time operator>>(istream&,Time);
};

Time :: Time()
{
    hour=minute=0;
}

Time :: Time(Time& a)
{
	hour=a.hour;
	minute=a.minute;
}

Time :: Time(int h, int m)
{
    setTime(h,m);
}

void Time :: setTime(int h, int m)
{
 	hour=h;
 	minute=m;
 	format();
}

void Time :: format()
{
	while(minute>60)
	{
		hour++;
		minute=minute-60;
	}
}

void Time :: operator+(Time a)
{
	minute=minute+a.minute;
	hour=hour+a.hour;
	format();
}

void Time :: operator=(Time a)
{
	minute=a.minute;
	hour=a.hour;
}

bool Time :: operator<(Time a)
{
	if(hour<a.hour)
	return true;
	else if (hour>a.hour)
	return false;
	
	if(minute<a.minute)
	return true;
	else
	return false;
}

bool Time :: operator>(Time a)
{
	if(hour>a.hour)
	return true;
	else if (hour<a.hour)
	return false;
	
	if(minute>a.minute)
	return true;
	else
	return false;
}

void sort(Time *a,int b)
{
	Time temp;
	for(int i=0;i<b;i++)
	{
		for(int j=i;j<b;j++)
		{
			if(a[i]>a[j])
			{
				temp=a[i];
				a[i]=a[j];
				a[j]=temp;
			}
		}
	}
}

void Time :: input(istream &fin)
{
	int h,m;
	string s;
	fin>>s;
	h=(s[0]-'0')*10+s[1]-'0';
	m=(s[3]-'0')*10+s[4]-'0';
	setTime(h,m);
}

int main()
{
	ifstream fin;
	fin.open("B-large.in");
	ofstream fout;
	fout.open("B-large.txt");
	int N;
	fin>>N;
	for(int i=0;i<N;i++)
	{
		int turn;
		fin>>turn;
		
		int NA,NB;
		fin>>NA>>NB;
		
		Time turnaround;
		turnaround.setTime(0,turn);
		Time *depA=new Time[NA];
		Time *arA=new Time[NA];
		Time *depB=new Time[NB];
		Time *arB=new Time[NB];
		for(int j=0;j<NA;j++)
		{
			depA[j].input(fin);
			arA[j].input(fin);
			arA[j]+turnaround;
		}
		for(int j=0;j<NB;j++)
		{
			depB[j].input(fin);
			arB[j].input(fin);
			arB[j]+turnaround;
		}
		
		sort(depA,NA);
		sort(depB,NB);
		sort(arA,NA);
		sort(arB,NB);
		
		int trains_at_A=0;
		int trains_at_B=0;
		int k=0;
		for(int j=0;j<NA;j++)
		{
			if(depA[j]<arB[k] || k==NB)
			trains_at_A++;
			else
			k++;
		}
		k=0;
		for(int j=0;j<NB;j++)
		{
			if(depB[j]<arA[k] || k==NA)
			trains_at_B++;
			else
			k++;
		}
		fout<<"Case #"<<i+1<<": "<<trains_at_A<<" "<<trains_at_B<<endl;
	}
	system("pause");
    return 0;
}
