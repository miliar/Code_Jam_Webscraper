#include <cstdio>
#include <string>

using namespace std;

string P[1000];
char tmp[1000];
int v[600][600];
int rj[600*600];


int main(){
    int t;
    scanf("%d",&t);
    for(int test = 0;test<t;++test){
        int n,m;
        scanf("%d %d",&n,&m);
        memset(rj,0,sizeof(rj));
        for(int x = 0;x<n;++x){
            scanf("%s",tmp);
            P[x] = "";
            for(int y = 0;y<m/4;++y){
                if( tmp[y] == '0' ) P[x] += "0000";
                if( tmp[y] == '1' ) P[x] += "0001";
                if( tmp[y] == '2' ) P[x] += "0010";
                if( tmp[y] == '3' ) P[x] += "0011";
                if( tmp[y] == '4' ) P[x] += "0100";
                if( tmp[y] == '5' ) P[x] += "0101";
                if( tmp[y] == '6' ) P[x] += "0110";
                if( tmp[y] == '7' ) P[x] += "0111";
                if( tmp[y] == '8' ) P[x] += "1000";
                if( tmp[y] == '9' ) P[x] += "1001";
                if( tmp[y] == 'A' ) P[x] += "1010";
                if( tmp[y] == 'B' ) P[x] += "1011";
                if( tmp[y] == 'C' ) P[x] += "1100";
                if( tmp[y] == 'D' ) P[x] += "1101";
                if( tmp[y] == 'E' ) P[x] += "1110";
                if( tmp[y] == 'F' ) P[x] += "1111";
            }
        }
        /*  for(int x = 0;x<n;++x)
            printf("%s\n",P[x].c_str());
            printf("\n");*/
        int br = m*n;
        memset( v, 0, sizeof(v));
        int solc = 0;
        while(br > 0){
            for(int x = 0;x<n;++x)
                for(int y = 0;y<m;++y)
                    if(P[x][y] != '2' ) v[x][y] = 1; else v[x][y] = 0;
            
            int mx = 0, i = 0, j = 0;
            for(int x = 0; x < n;++x){
                for(int y = 0;y<m;++y){
                    int k1=0,k2=0;
                    if(P[x][y] == '2') continue;
                    if(y > 0 && P[x][y-1] != '2' && P[x][y-1] != P[x][y] ) k1 = v[x][y-1];
                    if(x > 0 && P[x-1][y] != '2' && P[x-1][y] != P[x][y] ) k2 = v[x-1][y];
                    int k = min(k1,k2);
                    if( P[x-k][y-k] != '2' && P[x-k][y-k] == P[x][y] ) ++k;
                    v[x][y] = max(v[x][y], k);
                    if( v[x][y] > mx ){
                        mx = v[x][y];
                        i = x;
                        j = y;
                    }
                }
                //  printf("\n");
            }
            if( rj[mx] == 0 ) ++solc;
            rj[mx]++;
            br -= mx*mx;
            //obrisi taj dio polja
            for(int x = i-(mx-1); x <= i; ++x){
                for(int y = j-(mx-1); y <=j;++y){
                P[x][y] = '2';
                }
            }
            /*            printf("%d %d %d\n",mx,i,j);
            for(int x = 0;x<n;++x)
                printf("%s\n",P[x].c_str());
                printf("\n");*/
        }
        printf("Case #%d: %d\n",test+1,solc);
        for(int x = 512*512; x > 0; --x)
            if(rj[x] > 0) printf("%d %d\n",x,rj[x]);
        //        printf("\n");
        //  break;
    }
    return 0;
}
