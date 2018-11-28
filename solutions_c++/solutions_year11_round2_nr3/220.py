#include<stdio.h>
#include<vector>
#include<string>
#include<math.h>
#include<algorithm>
using namespace std;

#define sz size()
#define pb push_back
#define len length()
#define clr clear()

#define eps 0.0000001
#define PI  3.14159265359

int n,brg,kraj,gh[55],resx[55],g[55][55];
bool mark[55];

FILE *ff=fopen("C-small-attempt0.in", "r"), *gg=fopen("C-small-attempt0.out", "w");

void idar(int x, int t, int tt) {

    if (kraj) return;

    int i,j,br,ok;

    if (x>n) {

        ok=1;
        for(i=1; i<=brg; i++) {
            br=0;
            for(j=0; j<=t; j++) mark[j]=false;
            for(j=1; j<=gh[i]; j++) if ( !mark[ resx[ g[i][j] ]] ) {
                br++;
                mark[ resx[ g[i][j] ]]=true;
            }
            if (br<t) ok=0;
        }

        if (ok) {
            fprintf(gg,"Case #%d: %d\n", tt, t);
            for(i=1; i<=n; i++) { fprintf(gg,"%d ", resx[i]); }
            fprintf(gg,"\n");
            kraj=true;
        }

    } else {

        for(i=1; i<=t; i++) {
            resx[x]=i;
            idar(x+1,t,tt);
        }
    }
    return;
}

int main() {

    int m,tt,ttt,p,i,j,sh,k,mm,res,v[55],u[55],st[55];

    fscanf(ff,"%d", &ttt);
    for(tt=1;tt<=ttt;tt++) {

        printf("%d\n", tt);
        fscanf(ff,"%d%d", &n, &m);
        for(i=0; i<m; i++) fscanf(ff,"%d", &u[i]);
        for(i=0; i<m; i++) {
            fscanf(ff,"%d", &v[i]);
            if (v[i]>u[i]) { p=u[i]; u[i]=v[i]; v[i]=p; }
        }

        for(i=0; i<m; i++)
          for(j=i+1; j<m; j++) if (u[i]>u[j] || (u[i]==u[j] && v[i]<v[j])) {
              p=u[i]; u[i]=u[j]; u[j]=p;
              p=v[i]; v[i]=v[j]; v[j]=p;
          }

        sh=0; brg=0; mm=5555;
        for(i=1; i<=n; i++) {
           sh++;
           st[sh]=i;
           for(j=0; j<m; j++) if (u[j]==i) {
               brg++;
               gh[brg]=1;
               g[brg][1]=i;
               k=sh;
               do {
                   k--;
                   gh[brg]++;
                   g[brg][gh[brg]]=st[k];
               } while( st[k]!=v[j] );
               sh=k+1;
               st[sh]=i;
               if (gh[brg] < mm) mm=gh[brg];
           }
        }

        brg++;
        gh[brg]=0;
        k=sh;
        do {
            gh[brg]++;
            g[brg][gh[brg]]=st[k];
            k--;
        } while( k>0 );
        if (gh[brg] < mm) mm=gh[brg];

        /*printf("-> %d\n", brg);
        for(i=1; i<=brg; i++) {
           printf("%d: ", i);
           for(j=1; j<=gh[i]; j++) printf("%d ", g[i][j]);
           printf("\n");
        }*/

        if (brg==1) {
            fprintf(gg,"Case #%d: %d\n", tt, n);
            for(i=1; i<=n; i++) { fprintf(gg,"%d ", i); }
            fprintf(gg,"\n");
        } else {
            kraj=false;
            for(res=mm; res>=1; res--) if (!kraj) {
                idar(1,res,tt);
            }
        }
        printf("-> %d\n", tt);
    }

    fclose(ff); fclose(gg);

    return 0;
}
