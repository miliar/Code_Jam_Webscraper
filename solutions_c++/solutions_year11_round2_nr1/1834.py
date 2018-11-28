#include<iostream>
#include<string>
#include<conio.h>

using namespace std;

#define min(a,b) (a<b?a:b)
#define max(a,b) (a<b?b:a)
#define Size(x) (int)x.size()
#define FORI(i,n) for(int i = 0; i < n; i++)
#define FORB(i,be,en) for(int i = be; i <= en; i++)
#define Check1(i,j) (int)(a[i][j]=='1')?(int)1:(int)0

char a[101][101];
int b[101],c[101];
float wp[101],owp[101],oowp[101];

int n;

int main() {
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);
    int T,t;
    cin >> T;
    FORI(t,T) {
        printf("Case #%d:\n",t+1);
        scanf("%d",&n);
        cin.ignore();
        FORI(i,n) {
            b[i] = 0;
            c[i] = 0;
            FORI(j,n) {
                scanf("%c",&a[i][j]);
                if (a[i][j] == '1') b[i]++;
                if (a[i][j] == '0' || a[i][j] == '1') c[i]++;
            }
            cin.ignore();
            wp[i] = b[i]*1.0/c[i];
        }
        //tinh owp, oowp
        FORI(i,n) {
            float tong = 0.0;
            float o = 0.0;
            FORI(j,n) if (i!=j && a[i][j]!='.') {
                int temp = 0;
                if (a[j][i]=='1') temp = 1;
                tong += (b[j]-temp)*1.0/(c[j]-1);
                //cout << temp;
                //cout << j << "=" << b[j] << "," << c[j] << "," << tong << endl;
            }
            owp[i] = tong*1.0 / c[i];
            //cout << tong << " " << owp[i] << endl;getch();
        }
        
        FORI(i,n) {
            float tong = 0.0;
            FORI(j,n) if (i!=j && a[i][j]!='.') {
                tong += owp[j];
            }
            oowp[i] = tong*1.0 / c[i];
        }
        FORI(i,n-1) printf("%.6f\n",0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]);
        if (t < T-1) printf("%.6f\n",0.25*wp[n-1]+0.5*owp[n-1]+0.25*oowp[n-1]);
        else printf("%.6f",0.25*wp[n-1]+0.5*owp[n-1]+0.25*oowp[n-1]);
    }

    fclose(stdout);
    return 0;
}
