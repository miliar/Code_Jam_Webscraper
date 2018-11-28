#include <stdio.h>
#include <iostream>
#include <string>
using namespace std;

long tn,n,k; 

main()
{string ans[50];
 ans[1]="005";
 ans[2]="027";
 ans[3]="143";
 ans[4]="751";
 ans[5]="935";
 ans[6]="607";
 ans[7]="903";
 ans[8]="991";
 ans[9]="335";
 ans[10]="047";
 ans[11]="943";
 ans[12]="471";
 ans[13]="055";
 ans[14]="447";
 ans[15]="463";
 ans[16]="991";
 ans[17]="095";
 ans[18]="607";
 ans[19]="263";
 ans[20]="151";
 ans[21]="855";
 ans[22]="527";
 ans[23]="743";
 ans[24]="351";
 ans[25]="135";
 ans[26]="407";
 ans[27]="903";
 ans[28]="791";
 ans[29]="135";
 ans[30]="647";
 freopen("sec.in","r",stdin);
 freopen("sec.out","w",stdout);
 scanf("%d",&tn);
 for(k=0;k<tn;k++)
 {
    scanf("%d",&n);
    cout<<"Case #"<<k+1<<": "<<ans[n]<<endl;
 }
}
