#include <iostream>
#include <algorithm>
#include <string>
#include <cstdio>
#define M 100

using namespace std;

char S[M][M];
int nmatch[M]; // # of matches for each team
int nwin[M]; // # of winned matches for each team
double WP[M]; 
double OWP[M];
double OOWP[M];

bool build_nmatch(int N)
{
  //printf("nmatch results\n");
  for(int i=0; i!=N; i++) {
    nmatch[i] = 0;
    nwin[i] = 0;
    for(int j=0; j!=N; j++) {
      if(S[i][j]!='.') {
        nmatch[i] ++;
        if(S[i][j]=='1')
          nwin[i] ++;
      }
    }
    //printf("i=%d, nmatch=%d, nwin=%d\n", i, nmatch[i],nwin[i]);
  }

  return true;
}

bool build_WP(int N)
{
  //printf("WP results\n");
  for(int i=0; i!=N; i++) {
    WP[i] = double(nwin[i])/nmatch[i];
    //printf("i=%d, WP=%lf\n", i, WP[i]);
  }

  return true;
}

bool build_OWP(int N)
{
  //printf("OWP results\n");
  for(int i=0; i!=N; i++) {
    OWP[i] = 0;
    int count = 0;
    double ewp = 0;
    for(int j=0; j!=N; j++) {
      if(S[i][j]!='.') {
        if(S[i][j]=='1') { // i wins 
          ewp = double(nwin[j])/(nmatch[j]-1);
        }
        else { // j wins
          ewp = double(nwin[j]-1)/(nmatch[j]-1);
        }
        count++;
        OWP[i] += (ewp-OWP[i])/count;
      }
    }
    //printf("i=%d, OWP=%lf\n", i, OWP[i]);
  }
  
  return true;
}

bool build_OOWP(int N)
{
  //printf("OOWP results\n");
  for(int i=0; i!=N; i++) {
    OOWP[i] = 0;
    int count = 0;
    for(int j=0; j!=N; j++) {
      if(S[i][j]!='.') {
        count ++;
        OOWP[i] += (OWP[j]-OOWP[i])/count;
      }
    }
    //printf("i=%d, OOWP=%lf\n", i, OOWP[i]);
  } 

  return true;
}


int main()
{
	//freopen("test.txt","r",stdin);freopen("test.out","w",stdout);
	//freopen("A-small.in","r",stdin);freopen("A-small.out","w",stdout);
	freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);
	int testcase;
	cin >> testcase;
	for (int caseId=1;caseId<=testcase;caseId++)
	{
		int N;
    cin >> N;
    for(int i=0; i!=N; i++) {
      for(int j=0; j!=N; j++) {
        cin >> S[i][j];
      }
    }
    build_nmatch(N);
    build_WP(N);
    build_OWP(N);
    build_OOWP(N);

		printf("Case #%d:\n",caseId);
    for(int i=0; i!=N; i++) {
      double result = 0;
      result = 0.25*WP[i]+0.5*OWP[i]+0.25*OOWP[i];
		  printf("%lf\n", result);
    }
	}

	return 0;
}
