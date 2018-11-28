#include <iostream>
#include <string>
#include <vector>

using namespace std;

void Output(const char *str)
{
	static int x = 0;
	x++;
	printf("Case #%d: %s\n", x, str);
}

void Output(long long ans)
{
	static int x = 0;
	x++;
	printf("Case #%d: %I64d\n", x, ans);
}

void solve()
{
	int N, K;
	scanf("%d%d", &N, &K);
	char buf[50][50];
	for(int i = 0; i < N; i++) {
		scanf("%s",buf[i]);
	}
	
	char ans[100];
	bool red = false, blue = false;
	
	char str1[100], strr[100], strb[100];
	for(int i = 0; i < K; i++) {
		strr[i] = 'R';
		strb[i] = 'B';
	}
	strr[K] = '\0';
	strb[K] = '\0';
	
	/*
	// route
	for(int i = 0; i < N; i++) {
		string tmp = "";
		for(int j = 0; j< N; j++) {
			if( buf[i][j] != '.' ) {
				tmp += string(buf[i]+j, buf[i]+j+1);
			}
			buf[i][j] = '.';
		}
		int len = tmp.length();
		for(int j = 0; j < len; j++) {
			buf[i][j] = tmp[j];
		}
	}
	// check
	for(int i = 0; i< N; i++) {
		for(int j = 0; j < N; j++) {
			str1[j] = buf[i][j];
		}
		str1[N] = '\0';
		if( strstr(str1, strr) != NULL ) {
			red = true;
		}
		if( strstr(str1, strb) != NULL ) {
			blue = true;
		}
	}	
	for(int j = 0; j < N; j++) {
		for(int i = 0; i< N; i++) {
			str1[i] = buf[i][j];
		}
		str1[N] = '\0';
		if( strstr(str1, strr) != NULL ) {
			red = true;
		}
		if( strstr(str1, strb) != NULL ) {
			blue = true;
		}
	}
	for(int i = -N; i< 2*N; i++) {
		for(int j = 0; j < N; j++) {
			str1[j] = '.';
			if( i+j < 0 || i+j >= N ) continue;
			str1[j] = buf[i+j][j];
		}
		str1[N] = '\0';
		if( strstr(str1, strr) != NULL ) {
			red = true;
		}
		if( strstr(str1, strb) != NULL ) {
			blue = true;
		}
	}
	for(int i = -N; i< 2*N; i++) {
		for(int j = 0; j < N; j++) {
			str1[j] = '.';
			if( i-j < 0 || i-j >= N ) continue;
			str1[j] = buf[i-j][j];
		}
		str1[N] = '\0';
		if( strstr(str1, strr) != NULL ) {
			red = true;
		}
		if( strstr(str1, strb) != NULL ) {
			blue = true;
		}
	}*/
	// ¾µÏñ 
	for(int i = 0; i < N; i++) {
		string tmp = "";
		for(int j = 0; j< N; j++) {
			if( buf[i][j] != '.' ) {
				tmp += string(buf[i]+j, buf[i]+j+1);
			}
			buf[i][j] = '.';
		}
		int len = tmp.length();
		for(int j = 0; j < len; j++) {
			buf[i][j+(N-len)] = tmp[j];
		}
		// Output(buf[i]);
	}
	// check 
	for(int i = 0; i< N; i++) {
		for(int j = 0; j < N; j++) {
			str1[j] = buf[i][j];
		}
		str1[N] = '\0';
		if( strstr(str1, strr) != NULL ) {
			red = true;
		}
		if( strstr(str1, strb) != NULL ) {
			blue = true;
		}
	}	
	for(int j = 0; j < N; j++) {
		for(int i = 0; i< N; i++) {
			str1[i] = buf[i][j];
		}
		str1[N] = '\0';
		if( strstr(str1, strr) != NULL ) {
			red = true;
		}
		if( strstr(str1, strb) != NULL ) {
			blue = true;
		}
	}
	for(int i = -N; i< 2*N; i++) {
		for(int j = 0; j < N; j++) {
			str1[j] = '.';
			if( i+j < 0 || i+j >= N ) continue;
			str1[j] = buf[i+j][j];
		}
		str1[N] = '\0';
		if( strstr(str1, strr) != NULL ) {
			red = true;
		}
		if( strstr(str1, strb) != NULL ) {
			blue = true;
		}
	}
	for(int i = -N; i< 2*N; i++) {
		for(int j = 0; j < N; j++) {
			str1[j] = '.';
			if( i-j < 0 || i-j >= N ) continue;
			str1[j] = buf[i-j][j];
		}
		str1[N] = '\0';
		if( strstr(str1, strr) != NULL ) {
			red = true;
		}
		if( strstr(str1, strb) != NULL ) {
			blue = true;
		}
	}
	
	if( red && blue ) Output("Both");
	if( red && !blue ) Output("Red");
	if( !red && blue ) Output("Blue");
	if( !red && !blue ) Output("Neither");
}

void GCJ2010_R1A_001()
{
	int T;
	scanf("%d", &T);
	while(T--) {
		solve();
	}
}

int main()
{
	GCJ2010_R1A_001();
	return 0;
}

