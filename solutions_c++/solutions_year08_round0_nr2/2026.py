#include<iostream>
#include<vector>
#include<utility>
#include<algorithm>
// #include<fstream>
#include <stdio.h>

#
using namespace std;

typedef pair<int,int> Time;
bool earlier (Time t1, Time t2)
{
	if (t1.first < t2.first)
		return true;
	else if (t1.first == t2.first)
		return t1.second < t2.second;
	else
		return false;
}

Time add(Time t, int T)
{
	Time t1;
	t1.second = (t.second+T)%60;
	t1.first = t.first + (t.second+T)/60;
	return t1;
}

int main()
{
	int NA,NB,T,N, A,B;
	int k, i, j;
	Time t1,t2,p;
	vector<Time> arr_A, dep_A, arr_B,dep_B;
	
	FILE *fin, *fout;
	fin = fopen("B-large.in","r");
	fout = fopen("B-large.out","w");
	
	if(!fin)
	{
		cout << "Input file not opened!";
		return 0;
	}
	if(!fout)
	{
		cout << "Output file not opened!";
		return 0;
	}
	fscanf(fin,"%d\n",&N);

	for (k=0; k<N; k++)
	{
		cout << "TEST CASE: " << k+1 << endl;
		A=0; B=0;
		fscanf(fin,"%d\n",&T);
		fscanf(fin,"%d %d",&NA,&NB);

		for (i=0; i<NA; i++)
		{
			fscanf(fin,"%d:%d %d:%d\n",&t1.first,&t1.second,&t2.first,&t2.second);
			dep_A.push_back(t1);
			arr_B.push_back(t2);
		}

		for (i=0; i<NB; i++)
		{
			fscanf(fin,"%d:%d %d:%d",&t1.first,&t1.second,&t2.first,&t2.second);
			dep_B.push_back(t1);
			arr_A.push_back(t2);
		}
		sort(arr_A.begin(), arr_A.end(), earlier);
		sort(arr_B.begin(), arr_B.end(), earlier);
		sort(dep_A.begin(), dep_A.end(), earlier);
		sort(dep_B.begin(), dep_B.end(), earlier);
		
		arr_A.push_back(pair<int,int>(26,0));
		arr_B.push_back(pair<int,int>(26,0));

// 		for (i=0; i<arr_A.size(); i++)
// 		{
// 			p = add(arr_A[i],T);
// 			cout << arr_A[i].first << ":" << arr_A[i].second <<" becomes " << p.first<< ":" << p.second<<"\n";
// 		}
// 		cout << "******\n";
		for (i=0,j=0; i<dep_A.size();)
		{
			p = add(arr_A[j],T);
			cout << i<<" A :-   ";
			if(!earlier(dep_A[i],p))
			{
				cout << "don't need new train for " << i<< " as " << dep_A[i].first<<":"<< dep_A[i].second << " >= " << p.first << ":" << p.second<<endl;
				i++;
				j++;
			}
			else
			{
				cout<< "need new train for " << i<< " as " << dep_A[i].first<<":"<< dep_A[i].second << " < " << p.first << ":" << p.second<<endl;
				i++;
				A++;
			}
		}
		cout << "Size is " << dep_B.size()<<endl;
		for (i=0,j=0; i<dep_B.size();)
		{
			p = add(arr_B[j],T);
			cout << i<<" B :-   ";
			if(!earlier(dep_B[i],p))
			{
				cout << "don't need new train for " << i<< " as " << dep_B[i].first<<":"<< dep_B[i].second << " >= " << p.first << ":" << p.second<<endl;
				i++;
				j++;
				
			}
			else
			{
				cout<< "need new train for " << i<< " as " << dep_B[i].first<<":"<< dep_B[i].second << " < " << p.first << ":" << p.second<<endl;
				i++;
				B++;
			}
		}
		fprintf(fout, "Case #%d: %d %d\n", k+1,A,B);
		dep_A.clear();
		arr_B.clear();
		dep_B.clear();
		arr_A.clear();
	}
	fclose(fin);
	fclose(fout);
	return 0;
}
