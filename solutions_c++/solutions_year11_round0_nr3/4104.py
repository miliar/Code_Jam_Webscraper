#include <iostream>
#include <fstream>
#include <cstdlib>
#include <bitset>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

void performvi(vector<int> &vi)
{
  for(int i=0;i<vi.size();++i)
  {
    cout << vi[i] << "  ";
  }
  cout << endl;
}

int log2(int a)
{
  if (a==1)
  {
    return 0;
  }
  else
  {
    int val=0;
	while (a>=2)
	{
	  a/=2;
	  val++; 
	}
	return val+1;
  }
}

void add2patrick(int a,int b,int &res)
{
  int l1=log2(a);
  int l2=log2(b);
  int max;
  if (l1>l2)
    max=l1;
  else
    max=l2;
	
  bitset<20> numb1(a);
  bitset<20> numb2(b);
  bitset<20> total;
  int i;
  for(i=0;i<max;++i)
  {
    total[i]=numb1[i]^numb2[i];
  }
  res=0;
  int eks2=1;
  for(i=0;i<max;++i)
  {
    res+=(eks2*total[i]);
	eks2*=2;
  }
}

int exp2n(int a)
{
  if (a==0)
    return 1;
  else
  {
    return 2*exp2n(a-1);
  }
}

int sumall(vector<int> &vi)  
{
  int total=0;
  for(int i=0;i<vi.size();++i)
  {
    total+=vi[i];
  }
  return total;
}

int sumallpat(vector<int> &vi)
{
  if (vi.empty())
    return 0;
  if (vi.size()==1)
    return vi[0];
  if (vi.size()>1)
  {
    int restemp;
	add2patrick(vi[0],vi[1],restemp);
	for(int i=2;i<vi.size();++i)
	{
	  int rest=restemp;
	  add2patrick(rest,vi[i],restemp);
	}
	return restemp;
  }
}

void solveone(vector<int> &vi,bool &iscanbe,int &val)
{
  bitset<15> poss;
  
  iscanbe=false;
  int i,j;
  int totalposs=exp2n(vi.size());
  
  val=0;
  
  for(i=0;i<(totalposs/2);++i)
  {
    vector<int> vp1;
    vector<int> vp2;
    poss=i;
	for(j=0;j<vi.size();++j)
	{
	  if (poss[j]==0)
	  {
	    vp1.push_back(vi[j]);
	  }
	  else
	  {
	    vp2.push_back(vi[j]);
	  }
	}
	// cout << poss << endl;
	// performvi(vp1);
	// performvi(vp2);
	
	if (sumallpat(vp1)==sumallpat(vp2))
	{
	  // cout << "tes\n";
	  // cout << "sap1 = " << sumallpat(vp1) << endl;
	  // cout << "sap2 = " << sumallpat(vp2) << endl;
	  iscanbe=true;
	  int sa1=sumall(vp1);
	  int sa2=sumall(vp2);
	  // cout << "sa1 = " << sa1 << endl;
	  // cout << "sa2 = " << sa2 << endl;
	  if (sa1>sa2 && sa1!=0 && sa2!=0)
	  {
	    if (sa1>val)
		{
		  val=sa1;
		}
	  }
	  else if (sa1<=sa2  && sa1!=0 && sa2!=0)
	  {
	    if (sa2>val)
		{
		  val=sa2;
		}
	  }
	}
  }
  // cout << "nilai val : " << val << endl;
}

int main()
{
  ifstream fin;
  ofstream fout;
  fin.open("C-small-attempt0.in");
  fout.open("C-small-attempt0.out");
  int total;
  fin >> total;
  int i,j;
  for(i=0;i<total;++i)
  {
    vector<int> vi;
    int tone;
	fin >> tone;
	for(j=0;j<tone;++j)
	{
	  int val;
	  fin >> val;
	  vi.push_back(val);
	}
	// performvi(vi);
	bool iscanbe;
	int rest;
	solveone(vi,iscanbe,rest);
	if (iscanbe)
	{
	  fout << "Case #" << i+1 << ": " << rest << endl;
	}
	else
	{
	  fout << "Case #" << i+1 << ": NO" << endl;
	}
  }
  
  fin.close();
  fout.close();
  return 0;
}
