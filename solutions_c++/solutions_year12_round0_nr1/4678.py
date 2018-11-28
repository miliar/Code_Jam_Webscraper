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
vector<char> v;
	v.push_back('y');
	v.push_back('h');
	v.push_back('e');
	v.push_back('s');
	v.push_back('o');
	v.push_back('c');
	v.push_back('v');
	v.push_back('x');
	v.push_back('d');
	v.push_back('u');
	v.push_back('i');
	v.push_back('g');
	v.push_back('l');
	v.push_back('b');
	v.push_back('k');
	v.push_back('r');
	v.push_back('z');
	v.push_back('t');
	v.push_back('n');
	v.push_back('w');
	v.push_back('j');
	v.push_back('p');
	v.push_back('f');
	v.push_back('m');
	v.push_back('a');
	v.push_back('q');
fin.ignore(100,'\n');
vector<int> result;
for(int i=0; i<casenum;i++)
{
	char s[1000];
	
	fin.getline(s,1000);
	for(int j=0; j<1000; j++)
	{
		if((s[j]<='z')&&(s[j]>='a'))
		{
			s[j]=v[s[j]-'a'];

		}
			}
	fout<<"Case #"<<i+1<<": ";

	for(int j=0; s[j]!=NULL&&(j<1000);j++)
	{
		fout<<s[j];
	}
	fout<<endl;


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

