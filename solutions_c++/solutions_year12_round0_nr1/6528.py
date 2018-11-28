#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>

using namespace std;

#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)
#define foreach(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)

typedef long long ll;
string s;

char charset[] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};
char *conv;

//string tmp = "ejp mysljylc kd kxveddknmc re jsicpdrysi";

void calc(){
	char tmp[512];
	cin.getline(tmp, 512);

	int length = ((string)tmp).length(), i = 0;
	
	//char *orig = (char*)tmp.c_str();
	char *orig = tmp;
	conv = (char*)malloc(sizeof(char) * length);
	char *convTmp = conv;

	for(i = 0; i < length; i++){
		if((*orig) >= 'a' && (*orig) <= 'z'){
			(*convTmp) = charset[(*orig) - 'a'];
		}
		else{
			(*convTmp) = (*orig);
		}
		orig++;convTmp++;
	}
	(*convTmp) = '\0';
}

int main(void){
	int T, t = 1;
	scanf("%d", &T);
	char tmp[512];
	cin.getline(tmp, 512);
	REP(t, T){
		calc();
		printf("Case #%d: %s\n", t+1, conv);

	}
}
