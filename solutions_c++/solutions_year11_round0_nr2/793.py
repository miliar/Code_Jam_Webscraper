/*
 * in the name of god
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 */

#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

bool mark[30][30];
char invo[30][30];
int Q,I,O,n;
int cnt[30];

inline bool OP (char tmp){
	tmp-= 'A';

	for (int i=0;i<26;i++) if (mark[(int)tmp][i] && cnt[i])
		return true;

	return false;
}
/*********************************/
int main(){
	scanf ("%d", &Q);
	
	for (int t=1;t<=Q;t++){

		memset (cnt, 0, sizeof cnt);

		for (int i=0;i<26;i++)
			for (int j=0;j<26;j++)
				invo[i][j]= mark[i][j]= 0;

		scanf ("%d", &I);
		for (int i=1;i<=I;i++){
			char x,y,z;
			scanf (" %c %c %c", &x, &y, &z);
			invo[x-'A'][y-'A']= invo[y-'A'][x-'A']= z;
		}

		scanf ("%d", &O);
		for (int i=1;i<=O;i++){
			char x,y;
			scanf (" %c %c", &x, &y);
			mark[x-'A'][y-'A']= mark[y-'A'][x-'A']= true;
		}

		scanf ("%d", &n);

		vector <char> res;

		for (int i=1;i<=n;i++){

			char tmp;
			
			scanf (" %c", &tmp);

			if (res.empty()){
				res.push_back (tmp);
				cnt[tmp-'A'] ++;
			}

			else if (invo[tmp-'A'][res.back()-'A']!=0){
				
				tmp= invo[tmp-'A'][res.back()-'A'];
				
				cnt[res.back()-'A']--;
				cnt[tmp-'A']++;
				
				res.pop_back ();
				res.push_back (tmp);
			}

			else if (OP(tmp)){
				res.clear();
				memset (cnt, 0, sizeof cnt);
			}

			else{
				cnt[tmp-'A']++;
				res.push_back (tmp);
			}
		}

		printf ("Case #%d: [" , t);
		for (int i=0;i<(int)res.size();i++){
			if (i!=0)
				printf (", ");
			printf ("%c", res[i]);
		}
		printf ("]\n");
	}

	return 0;
}
