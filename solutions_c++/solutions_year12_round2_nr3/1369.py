using namespace std;
#include <iostream>
#include <vector>
#include <map>
#include <cstdlib>
typedef vector<int> ivector;
//typedef vector< ivector > myset_t;


map<int, ivector> mymap;
int found = 0;

int sumv(vector<int>& vi)
{
	int i, s = 0;
	for(i = 0;i < vi.size(); i++) {
		s += vi[i];
	}
	return s;
}

void outputset(ivector& vi)
{
	int i, s = vi.size();
	for(i = 0;i < s; i++) {
		cout << vi[i] << " ";
	}
	cout << endl;
}

bool subset(ivector& vi)
{
	if(vi.size() == 0) return true;
	else {
		//outputset(vi);
		int s = sumv(vi);
		if( mymap[s].size() == 0) {
			mymap[s] = vi;
			//cout << "mymap[" << s << "] = ";
			//outputset(mymap[s]);
		}
		else if(mymap[s] == vi) return true;
		else {
			outputset(mymap[s]);
			outputset(vi);
			//cout << "found\n";
			return false;
		}
		
		int i, j, size = vi.size();
		vector<int> vi2;
		for( i = 0; i < size; i++) {
			vi2.clear();
			for(j = 0; j < size; j++) {
				if(i != j) vi2.push_back( vi[j] );
				//outputset(vi2);
			}
			//outputset(vi2);
			if(false == subset(vi2)) return false;
		}
	}
	return true;
}

void compute(int n, int ns[])
{
	mymap.clear();
	int i; 
	ivector vi;
	for(i = 0;i < n; i++){
		vi.push_back(ns[i]);
	}
	
	if(true == subset(vi))
		cout << "Impossible" <<endl;
	//else
		
}

int compare (const void * a, const void * b)
{
  return ( *(int*)a - *(int*)b );
}

int main()
{
	int ncase;
	cin >> ncase;
	
	int i; 
	for(i = 0;i < ncase; i++){
		int nj;
		cin >> nj;
		
		int sj[nj];
		int j;
		for(j = 0; j < nj; j++) {
			cin >> sj[j];
		}
		qsort (sj, nj, sizeof(int), compare);
		
		cout << "Case #" << i+1 << ":"<<endl;
		compute(nj,sj);
	}
}
