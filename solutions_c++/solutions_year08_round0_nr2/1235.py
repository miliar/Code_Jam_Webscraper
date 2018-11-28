#include<iostream>
#include<fstream>
#include<string>
#include<algorithm>
using namespace std;
/*
ifstream fin("B.in");
ofstream fout("B.out");
int n, na, nb, t;
struct Trip
{
	string start, end;
	bool set;
	int flag;

	void exchange()
	{
		string temp = start;
		start = end;
		end = temp;
	}
};
Trip train[200];

string addtime(string now, int min);
bool f(Trip a, Trip b);

int main()
{
	int i = 0, j, k,ans[2], tflag, tn;
	string etime;
	
	fin>>n;
	while(i < n)
	{
		i ++;

		/*---------获取输入------------*/
/*		fin>>t;				//turnaround time
		fin>>na>>nb;		//A站和B站的列车数
		ans[0] = na; ans[1]= nb;
		tn = na+nb;
		for(j = 0; j < na; ++ j){
			fin>>train[j].start>>train[j].end;
			if(train[j].start > train[j].end) train[j].exchange();
			train[j].flag = 0;
			train[j].set = false;
		}
		for(j = na; j < tn; ++ j){
			fin>>train[j].start>>train[j].end;
			if(train[j].start > train[j].end) train[j].exchange();
			train[j].flag = 1;
			train[j].set = false;
		}
		sort(train, train+tn, f);



		for(j = 0; j < tn; ++ j)
		{
			if(!train[j].set)
			{
				train[j].set = true;
				tflag = 1-train[j].flag; 
				etime = addtime(train[j].end, t);

				for(k = j+1; k < tn; ++ k)
				{
					if(train[k].set) continue;
					if(train[k].flag == tflag && train[k].start >= etime){
						train[k].set = true; 
						ans[tflag] --;
						tflag = 1-train[k].flag;
						etime = addtime(train[k].end, t);
					}
				}
			}
		}
		fout<<"Case #"<<i<<": "<<ans[0]<<" "<<ans[1]<<endl;
	}
	return 0;
}

string addtime(string now, int min)
{
	int m = (now[3]-'0')*10+(now[4]-'0');
	m += min;
	int h = (now[0]-'0')*10+(now[1]-'0');
	h += m/60;
	m %= 60;
	string end = now;
	end[0] = (char)(h/10+'0');
	end[1] = (char)(h%10+'0');
	end[3] = (char)(m/10+'0');
	end[4] = (char)(m%10+'0');
//	cout<<endl;
//	cout<<now<<"+"<<min<<"="<<end<<endl;
	return end;
}
bool f(Trip a, Trip b)
{
	if(a.end == b.end) return a.start<b.start;
	return a.end<b.end;
}
*/

ifstream fin("B-small.in");
ofstream fout("B-small.out");
struct Trip{
	string start, end;
	int index;
	bool set;

	void exchange()
	{
		string temp = start;
		start = end;
		end = temp;
	}
} train[200];
/*bool f(Trip a, Trip b)
{
	if(a.end == b.end) return a.start<b.start;
	return a.end<b.end;
}*/
bool f(Trip a, Trip b)
{
	if(a.start == b.start) return a.end<b.end;
	return a.start<b.start;
}
string addTime(string now, int t)
{
	int h, m;
	h = (now[0]-'0')*10 + (now[1]-'0');
	m = (now[3]-'0')*10 + (now[4]-'0');
	m = m+t;
	h = h + m/60;
	m = m%60;

	string ans = "00:00";
	ans[0] = (char)(h/10+'0');
	ans[1] = (char)(h%10+'0');
	ans[3] = (char)(m/10+'0');
	ans[4] = (char)(m%10+'0');
	return ans;
}

int main()
{
	int n, na, nb, nab, t, ans[2];
	int j, k;//循环变量；
	fin>>n;
	for(int i = 0; i < n; ++ i){
		fin>>t>>na>>nb;
		nab = na+nb;
		ans[0] = na; ans[1] = nb;

		for(j = 0; j < na; ++ j){
			fin>>train[j].start>>train[j].end;
			if(train[j].start > train[j].end) train[j].exchange();
			train[j].set = false;
			train[j].index = 0;
		}
		for(j = na; j < nab; ++ j){
			fin>>train[j].start>>train[j].end;
			if(train[j].start > train[j].end) train[j].exchange();
			train[j].set = false;
			train[j].index = 1;
		}
		sort(train, train+nab, f);

		string now; int nIndex;
		for(j = 0; j < nab; ++ j){
			if(train[j].set) continue;
			train[j].set = true;

			nIndex = 1-train[j].index;
			now = addTime(train[j].end, t);			
			for(k = j+1; k < nab; ++ k){
				if(train[k].set) continue;
				if((train[k].index == nIndex) && (train[k].start >= now)){
					train[k].set = true; 
					ans[nIndex] --;
					nIndex = 1 - train[k].index;
					now = addTime(train[k].end, t);
				}
			}
		}
		fout<<"Case #"<<(i+1)<<": "<<ans[0]<<" "<<ans[1]<<endl;
	}
	return 0;
}
