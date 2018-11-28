#include<iostream>
#include<cstdio>
#include<vector>
#include<string>

using namespace std;

struct bd {
    string s[5];
};

int main()
{
    int t,nc=0;
    scanf("%d",&t);
    while(t--) {
        char bd[5][5];
        vector<string> vec;
        string str;

        for(int i=0; i<4; i++)
            scanf("%s",bd[i]);
        for(int i=0; i<4; i++)
            vec.push_back(bd[i]);
        for(int i=0; i<4; i++) {
            str = "";
            for(int j=0; j<4; j++) {
                str += bd[j][i];
            }
            vec.push_back(str);
        }

        str="";
        for(int i=0; i<4; i++) {
            str += bd[i][i];
        }
        vec.push_back(str);
        str="";
        for(int i=3,j=0; i>=0; i--,j++) {
            str += bd[j][i];
        }
        vec.push_back(str);

        int sp=0,xw=0,ow=0;
        for(int i=0; i<vec.size(); i++) {
            int nX=0,nO=0;
            for(int j=0; j<4; j++) {
                if(vec[i][j]=='X') {
                    nX++;
                    continue;
                } else if(vec[i][j]=='O') {
                    nO++;
                    continue;

                } else if(vec[i][j]=='T') {
                    nX++;
                    nO++;
                    continue;
                } else {
                    sp++;
                }
            }
            if(nX==4)
                xw++;
            else if(nO==4)
                ow++;
        }
        if(xw > ow) {
            printf("Case #%d: X won\n",++nc);
            continue;
        } else if(ow > xw) {
            printf("Case #%d: O won\n",++nc);
            continue;
        } else if(ow == xw and !sp) {
            printf("Case #%d: Draw\n",++nc);
            continue;
        } else {
            printf("Case #%d: Game has not completed\n",++nc);
            continue;
        }
        cin>>str;
    }
    return 0;
}
