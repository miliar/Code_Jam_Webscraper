#include <iostream>

using namespace std;

int main()
{

	int t,i,j,z;
	char a[4][4];
	int cxh,coh,cxv,cov,cxmd,comd,cxpd,copd;
	bool flagx,flagy,flagdraw,flagnend;

	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
    cin>>t;

    for (z=0;z<t;z++) {

        for (i=0;i<4;i++) {
            for (j=0;j<4;j++)  {
                cin>>a[i][j];
//              cout<<a[i][j];
            }
        }

        flagx=0;
        flagy=0;
        flagdraw=0;
        flagnend=0;

        for (i=0;i<4;i++) {
            cxh=0;
            coh=0;
            cxv=0;
            cov=0;
            cxmd=0;
            comd=0;
            cxpd=0;
            copd=0;
            for (j=0;j<4;j++)  {
                if ((a[i][j]=='X')||(a[i][j]=='T')) cxh++;
                if ((a[i][j]=='O')||(a[i][j]=='T')) coh++;
                if ((a[j][i]=='X')||(a[j][i]=='T')) cxv++;
                if ((a[j][i]=='O')||(a[j][i]=='T')) cov++;
                if ((a[j][j]=='X')||(a[j][j]=='T')) cxmd++;
                if ((a[j][j]=='O')||(a[j][j]=='T')) comd++;
                if ((a[j][3-j]=='X')||(a[j][3-j]=='T')) cxpd++;
                if ((a[j][3-j]=='O')||(a[j][3-j]=='T')) copd++;
                if (a[i][j]=='.') flagnend=1;
            }
            if (cxh==4||cxv==4||cxmd==4||cxpd==4) { flagx=1; break; }
            if (coh==4||cov==4||comd==4||copd==4) { flagy=1; break; }
        }
        
        if (flagx) { cout<<"Case #"<<z+1<<": X won"<<endl; continue; }
        if (flagy) { cout<<"Case #"<<z+1<<": O won"<<endl; continue; }
        if (flagnend) { cout<<"Case #"<<z+1<<": Game has not completed"<<endl; continue; }
        cout<<"Case #"<<z+1<<": Draw"<<endl;


    }


}