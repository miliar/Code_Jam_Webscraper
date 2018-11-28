#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#include <fstream>
using namespace std;

vector<long> g;
vector<long> ans;
vector<long> cnt;
long r, k ,n,t;

void get_data(ifstream &inp);
long getnum(long a);

int main()
{	
	string st;
	ifstream indata;
	cout << "Name of the file with the data: " << endl;
	cin >> st;
	indata.open(st.c_str());
	if (!indata.is_open())
	{
	cout << "Wrong file!" << endl;
	return 1;
	}
	cout << "Name the file with the output: " << endl;
	cin >> st;
	ofstream out(st.c_str());
	if(!out) {
	cout << "Cannot open file.\n";
	return 1;
	}
	indata >>t;
	cout << "t: " << t << endl;
	long answer, temp, count, sum,place,sp,sp2;
	bool bo, bo2;
	for (int i=0; i<t ;i++)
	{
		answer=0;
		sum=0;
		get_data(indata);
		for(int j=0; j<n ;j++){
			temp=0;
			count=0;
			place=j;
			sp2=j;
			bo=true;
			bo2=false;
			while(bo){
				if(((temp+g[place])<=k) && (!((bo2) && (place>=sp2)))){
					temp+=g[place];
					count++;
					place=count+j;
					sp=place;
					place=getnum(place);
					if (sp!=place)
						bo2=true;
					//cout << "place: " << place << " temp: " << temp << " j: " << j << " count: " << count << endl;
				}
				else
					bo=false;
			}	
			ans[j]=temp;
			cnt[j]=count;
			//cout << "ans[j]: " << ans[j] << " cnt[j]: " << cnt[j] << endl;
		}
		for(int j=0; j<r;j++){
			answer+=ans[sum];
			sum+=cnt[sum];
			sum=getnum(sum);
		}
		out << "Case #" << i+1 << ": " << answer << endl;
		//cout << "Case #" << i+1 << ": " << answer << endl;
	}
}
long getnum(long a)
{
	return (a%n);
}
void get_data(ifstream &inp)
{
	long st;
	g.clear();
	ans.clear();
	cnt.clear();
	inp >> r;
	inp >> k;
	inp >> n;
	//cout << "r: " << r << " k: " << k << " n: " << n << endl;
	for (int i=0; i< n; i++)
	{
		inp >> st;
		g.push_back(st);
		ans.push_back(0);
		cnt.push_back(0);
	}
}