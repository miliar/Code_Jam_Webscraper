#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <vector>

using namespace std;

char buf[100];
string str;
vector<string> vs;
string::iterator si;
double sol;
int paren;

void spc()
{
	while(*si == ' ') si++;
}

void parse()
{
	int i = 0;

	while(si != str.end() && *si!= '(' && *si != ' ' && *si != ')') {
		buf[i++] = *si;
		si++;
	}

	buf[i] = '\0';
	
	return;
}

bool haveChar(string t)
{
	int i;
	for(i=0; i<vs.size(); i++) {
		if(vs[i] == t) return true;
	}
	return false;

}

void start()
{
	string temp;
	double p;

	sol = 1.0;
	for(si = str.begin(); si != str.end(); spc()) {
		spc();
		if(*si == '(') {
			si++;
			spc();
			parse();
			p = atof(buf);
			sol *= p;
			spc();
			if(*si == ')') return;
			else {
				parse();
				if(haveChar(buf)) {
					spc();
				}	
				else {
					spc();
					si++;
					paren = 1;
					while(paren) {
						if(*si == '(') paren++;
						else if(*si == ')') paren--;
						si++;
					}
					spc();
				}
			}
		}
		else if(*si == ')') return;
		
	}
	

}

int main()
{
	freopen("01l.in", "r", stdin);
	freopen("01l.out", "w", stdout);

	int i, j, cas, now, nl, na, nc;
	scanf("%d\n",&cas);

	for(now = 1; now <= cas; now++) {
		str.erase(str.begin(), str.end());
		
		scanf("%d\n",&nl);
		for(i=0; i<nl; i++) {
			cin.getline(buf, 100);
			str += buf;
		}
		scanf("%d\n",&na);
		printf("Case #%d:\n",now);
		for(i=0; i<na; i++) {
			scanf("%s",buf);
			scanf("%s",buf);
			nc = atoi(buf);
			for(j=0; j<nc; j++) {
				scanf("%s",buf);
				vs.push_back(buf);
			}
			scanf("\n");
			start();
			printf("%.7lf\n",sol);		
			vs.clear();
		}

	}

	return 0;
}