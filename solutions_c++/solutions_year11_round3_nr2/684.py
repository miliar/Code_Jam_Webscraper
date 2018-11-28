#include<cstdio>
#include<cstring>
#include<vector>
#include<algorithm>
using namespace std;

int sf(long long a,long long b) {
  if (a > b) return 1;
  return 0;
}

int main() {
  FILE *fout = fopen("D:\\out.txt","w");
  FILE *fin = fopen("D:\\in.txt","r");

  long long t;

  fscanf(fin,"%lld",&t);

  for (long long ll = 0; ll < t; ll++ ) {
    long long time = 0;
    long long dist[1010];
    long long a[1010];
    memset(dist,0,sizeof(dist));
    long long l,n,c;
    long long tt;
    fscanf(fin,"%lld %lld %lld %lld",&l,&tt,&n,&c);
    for (int i = 0; i < c; i++ )
      fscanf(fin,"%lld",&a[i]);
    for (int i = 0; i < n; i++ )
      dist[i] = a[i%c] * 2;

      if (l == 0) {
        for (int i = 0; i < n; i++)
          time += dist[i];
        tt = time;
      }
      else {
        long long ndist[1010];
        int i = 0;
        while (time < tt) {
          ndist[i] = dist[i];
          time += dist[i++];
        }

        i--;
        ndist[i] = tt - (time - dist[i]);
        ndist[i+1] = dist[i] - ndist[i];

        long long pos = ndist[i+1];
        dist[i]  = pos;
        vector<long long> novi;
        for (;i < n; i++)
          novi.push_back(dist[i]);

        sort(novi.begin(),novi.end(),sf);

        for (i = 0; i < l;i++)
          novi[i] /= 2;

        for (i = 0; i < novi.size();i++)
          tt += novi[i];

      }

      fprintf(fout,"Case #%lld: ",ll+1);
      fprintf(fout,"%lld\n",tt);

  }

  return 0;

}


