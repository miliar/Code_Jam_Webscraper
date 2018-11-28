#include <stdio.h>
#include <string>
#include <stdlib.h>
#include <vector>
using namespace std;
char line[1000];
int t,l,a;
string question, st, tempst;
vector<string> features;

void analysis()
{
	int tp = question.find_first_of(' ');
	string fname = question.substr(0, tp);
	question = question.substr(tp, question.length());
	tp = 0; 
	while (question[tp] == ' ') tp++;
	question = question.substr(tp, question.length());
	tp = 0;
	int inum = 0;
	while (question[tp] >= '0' && question[tp]<='9') 
	{
		inum = inum * 10 + question[tp] - '0';
		tp++;
	}
	question = question.substr(tp, question.length());
	for (int i = 1; i <= inum; ++i)
	{
		tp = 0;
		while (question[tp] == ' ') tp++;
		question = question.substr(tp, question.length());
		tp = question.find_first_of(' ');
		string feature = question.substr(0, tp);
		features.push_back(feature);
		question = question.substr(tp, question.length());
	}
}

void findans()
{
	double ans;
	bool aflag;
	int tp,tk;
	string sw;
	int l1, l2, r1, r2;
	double weight;
	ans = 1.0;
	while (tempst != "")
	{
		tp = tempst.find_first_of('(');
		tk = tempst.find_last_of(')');
		tempst = tempst.substr(tp + 1, tk - tp - 1);
		tp = tempst.find_first_not_of(' ');
		tempst = tempst.substr(tp, tempst.length());
		tp = tempst.find_first_of(' ');
		if (tp != -1) sw = tempst.substr(0, tp);
		else sw = tempst.substr(0, tempst.length());
		weight = atof(sw.c_str());
		ans *= weight;
		tp = tempst.find_first_not_of(' ',tp);
		if (tp == -1) break;
		else
		{
			tk = tempst.find_first_of(' ', tp);
			string tp_feature = tempst.substr(tp, tk - tp);
			tp = tempst.find_first_not_of(' ', tk);
			tempst = tempst.substr(tp, tempst.length());
			l1 = tempst.find_first_of('(');
			tp = 1;
			for (l2 = l1 + 1; l2 < tempst.length(); ++l2)
			{
				if (tempst[l2] == '(') ++tp;
				if (tempst[l2] == ')') --tp;
				if (tp == 0) break;
			}

			r1 = tempst.find_first_of('(', l2);
			tp = 1;
			for (r2 = r1 + 1; r2 < tempst.length(); ++r2)
			{
				if (tempst[r2] == '(') ++tp;
				if (tempst[r2] == ')') --tp;
				if (tp == 0) break;
			}
			aflag = false;

			for (int i = 0; i < features.size(); ++i)
			{
				if (tp_feature.compare(features[i]) == 0) 
				{
					tempst = tempst.substr(l1, l2 - l1 + 1);
					aflag = true;	
				}
			}
			if (aflag == false)
			{
				tempst = tempst.substr(r1, r2 - r1 + 1);
			}
		}
	}
	printf("%.7lf\n", ans);


}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&t);
	for (int i = 1; i <= t; ++i)
	{
		printf("Case #%d:\n", i);
		scanf("%d\n",&l);
		st = "";
		for (int j = 1; j <= l; ++j)
		{
			gets(line);
			st += line;
			st += " ";
		}
		scanf("%d\n", &a);
		for (int j = 1; j <= a; j++)
		{
			gets(line);
			question = "";
			question += line;
			question += " ";
			features.clear();
			analysis();
			tempst = st;
			findans();
		}


	}
	return 0;
}