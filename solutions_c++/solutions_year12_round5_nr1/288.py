#include <algorithm>
#include <string>
#include <list>
#include <numeric>
#include <vector>
#include <math.h>
#include <set>
#include <map>
#include <sstream>
#include <stack>
#include <stdio.h>
#include <iostream>
using namespace std;

pair<int,int> prob[1000];
int times[1000];

void solveC(int t) {
	int n;
	cin>>n;

	for (int i=0;i<n;i++) {
		cin>>times[i];	
	}
	
	for (int i=0;i<n;i++) {
		int p;
		cin>>p;
		prob[i].first=p;
		prob[i].second=i;
	}
	
	sort(prob, prob+n);

	vector<int> answer;
	int i=n-1;
	while (i>=0) {
		vector<int> same;
		while (i>0 && prob[i].first == prob[i-1].first) {
			same.push_back(prob[i].second);
			i--;
		}
		same.push_back(prob[i].second);
		vector<pair<int,int> > timesforsame;
		for (int j=0; j<same.size(); j++) {
			timesforsame.push_back(make_pair(same[j],times[same[j]]));
		}
		sort(timesforsame.begin(), timesforsame.end());
		for (int j=0; j<timesforsame.size(); j++)
			answer.push_back(timesforsame[j].first);
		i--;
	}

	printf("Case #%d: ", t);
	for (int i=0;i<n;i++)
		cout<<answer[i]<<" ";
	cout<<endl;
}

int main()
{
	freopen("in.in", "rt", stdin);
	freopen("out.out", "wt", stdout);
	int t;
	cin>>t;
	for (int i=0;i<t;i++) {
		solveC(i+1);
	}
    return 0; 
} 