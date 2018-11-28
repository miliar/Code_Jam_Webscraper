#include <iostream>
#include <string>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <cstdio>
using namespace std;
int main(){
    freopen("A-large.in","r",stdin);
    freopen("Alout.out","w",stdout);
    int t;
    scanf("%d",&t);
    int k=0;
    while(t--){
        k++;
        string a[4];
        cin>>a[0]>>a[1]>>a[2]>>a[3];
        string result;
        for(int i=0;i<4;i++){
            string row="",column="";
            for(int j=0;j<4;j++){
                row+=a[i][j];
                if(a[i][j]=='.')
                    result="Game has not completed";
            }
            for(int k=0;k<4;k++){
                column+=a[k][i];
            }
            string s1="",s2="";
            s1+=a[0][0];s1+=a[1][1];s1+=a[2][2];s1+=a[3][3];
            s2+=a[0][3];s2+=a[1][2];s2+=a[2][1];s2+=a[3][0];
            sort(row.begin(),row.end());
            sort(column.begin(),column.end());
            sort(s1.begin(),s1.end());
            sort(s2.begin(),s2.end());
            if(row=="OOOT" || column=="OOOT" || s1=="OOOT" || s2=="OOOT" || row=="OOOO" || column=="OOOO" || s1=="OOOO" || s2=="OOOO"){
                result="O won";
                break;
            }
            else if(row=="TXXX" || column=="TXXX" || s1=="TXXX" || s2=="TXXX" || row=="XXXX" || column=="XXXX" || s1=="XXXX" || s2=="XXXX"){
                result="X won";
                break;
            }

        }
        if(!result.size())
            result="Draw";
        cout<<"Case #"<<k<<": "<<result<<endl;
    }
	return 0;
}
