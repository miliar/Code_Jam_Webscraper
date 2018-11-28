#include<fstream>
#include<cmath>
#include<string>
#include<vector>
using namespace std;

void mergeSort(int first, int last, vector<int>& v);

void merge(int first, int last,vector<int>& v);
int main(){
int casenum;
ifstream fin;
fin.open("input.txt");
ofstream fout;
fout.open("output.txt");

fin>>casenum;

int n,s, p;
vector<int> result;
for(int i=0; i<casenum;i++)
{
	vector<int> v;
	fin>>n>>s>>p;
	for(int j=0; j<n;j++)
	{
		int temp;
		fin>>temp;
		v.push_back(temp);
	}

	mergeSort(0,v.size()-1, v);
	int cutoff=p*3-2;
	if(cutoff<0) cutoff=0;
	int scutoff=p*3-4;
	if(scutoff<0) scutoff=0;
	int ccount=0;
	int scount=0;
	for(int j=0; (j<v.size())&&(v[j]>=cutoff);j++)
	{
		ccount++;
	}
	
	for(int j=ccount;j<v.size()&&(v[j]>=scutoff)&&(v[j]!=0);j++){
		scount++;
	}
	int num=ccount+((scount>s)?s:scount);
	
	result.push_back(num);

}







for(int i=0;i<result.size(); i++)
{
	fout<<"Case #"<<i+1<<": "<<result[i]<<endl;

}





}

void mergeSort(int first, int last, vector<int>& v)
{
	if(first<last){
	int mid= (first+last)/2;
	mergeSort(first, mid,v);
	mergeSort(mid+1,last,v);
	merge(first,last,v);
	}

}
void merge(int first, int last,vector<int>& v)
{
	int mid=(first+last)/2;
	int i=first;
	int j=mid+1;
	
	vector<int> temp;
	while(i<=mid&&j<=last)
	{
		if(v[i]>v[j])
		{
			temp.push_back(v[i++]);
		}
		else
			temp.push_back(v[j++]);

	}
	while(i<=mid)
		temp.push_back(v[i++]);
	while(j<=last)
		temp.push_back(v[j++]);
	for(int k=first;k<=last;k++)
		v[k]=temp[k-first];


}

