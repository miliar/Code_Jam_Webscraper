#include <iostream>

using namespace std;

void buildT(char *p);
bool compare( const char *s );

const int maxN = 500;
const int maxD = 5000;
const int maxL = 15;
const int abcLen = 26;
bool t[maxL][abcLen];
int N, D, L, cnt;

int main()
{
	char pattern[(abcLen+2)*maxL+1];
	char s[maxD][maxL+1];

	//cout << "debug1" << endl;

	cin >> L >> D >> N;
	//cout << L << ' ' << D << ' ' << N << endl;
	for(int i=0; i<D; i++){
		cin >> s[i];
		//cout << s[i] << endl;
	}
	//cout << "debug2" << endl;
	for(int i=1; i<=N; i++){
		/************************************
			Input Data
		*************************************/
		cin >> pattern;
		//cin.ignore(maxLen,'\n'); // skipping end-of-line
		/************************************
			Solve the Problem
		*************************************/
		buildT(pattern);
		cnt=0;
		for(int j=0; j<D; j++){
			cnt+=compare(s[j]);
			}
		/************************************
			Output Results
		*************************************/
		cout << "Case #" << i << ": " << cnt << endl;
		/* Debug
		cout << "----------------\n";
		for(int j=0; j<S; j++)
			cout << searchEngineNames[j] << endl;
		cout << "----------------\n";
		for(int j=0; j<Q; j++)
			cout << queries[j] << endl;
		*/
	}
	return 0;
}

void buildT(char *p)
{
	memset(t,0,sizeof(t));
	for(int i=0, j=0; i<L; i++, j++)
	{
		if(p[j]=='(')
		{
			for(j=j+1; p[j]!=')'; j++)
				t[i][p[j]-'a'] = true;
		}else{
			t[i][p[j]-'a'] = true;
		}
	}
}
bool compare( const char *s )
{
   /* Compare to the pattern: */
	bool r = true;
	for(int i=0; i<L; i++)
		if(!t[i][s[i]-'a'])
			return false;
    return true;
}