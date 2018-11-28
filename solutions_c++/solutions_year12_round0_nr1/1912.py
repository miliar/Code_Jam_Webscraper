#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <set>
#include <queue>
#include <map>
#include <cstdio>
#include <iomanip>
#include <sstream>
#include <iostream>
#include <cstring>
#define REP(i,x,v)for(int i=x;i<=v;i++)
#define REPD(i,x,v)for(int i=x;i>=v;i--)
#define FOR(i,v)for(int i=0;i<v;i++)
#define FORE(i,t) for (typeof(t.begin()) i=t.begin(); i!=t.end(); i++)
#define REMIN(x,y) (x)=min((x),(y))
#define REMAX(x,y) (x)=max((x),(y))
#define pb push_back
#define sz size()
#define mp make_pair
#define fi first
#define se second
#define ll long long
#define IN(x,y) ((y).find((x))!=(y).end())
#define un(v) v.erase(unique(ALL(v)),v.end())
#define LOLDBG
#ifdef LOLDBG
#define DBG(vari) cerr<<#vari<<" = "<<vari<<endl;
#define DBG2(v1,v2) cerr<<(v1)<<" - "<<(v2)<<endl;
#else
#define DBG(vari)
#define DBG2(v1,v2)
#endif
#define CZ(x) scanf("%d",&(x));
#define CZ2(x,y) scanf("%d%d",&(x),&(y));
#define CZ3(x,y,z) scanf("%d%d%d",&(x),&(y),&(z));
#define ALL(x) (x).begin(),(x).end()
#define tests int dsdsf;cin>>dsdsf;while(dsdsf--)
#define testss int dsdsf;CZ(dsdsf);while(dsdsf--)
using namespace std;
typedef pair<int,int> pii;
typedef vector<int> vi;
template<typename T,typename TT> ostream &operator<<(ostream &s,pair<T,TT> t) {return s<<"("<<t.first<<","<<t.second<<")";}
template<typename T> ostream &operator<<(ostream &s,vector<T> t){s<<"{";FOR(i,t.size())s<<t[i]<<(i==t.size()-1?"":",");return s<<"}"<<endl; }

int tlum[200];

int main()
{

    /*FOR(j,200) tlum[j]=j;
    FOR(i,3)
    {
        string s,t;
        getline(cin,s);
        getline(cin,t);
        FOR(j,s.sz) tlum[s[j]]=t[j];
    }
    FOR(j,200) printf("tlum[%d]=%d;\n",j,tlum[j]);
    */
    tlum[0]=0;
tlum[1]=1;
tlum[2]=2;
tlum[3]=3;
tlum[4]=4;
tlum[5]=5;
tlum[6]=6;
tlum[7]=7;
tlum[8]=8;
tlum[9]=9;
tlum[10]=10;
tlum[11]=11;
tlum[12]=12;
tlum[13]=13;
tlum[14]=14;
tlum[15]=15;
tlum[16]=16;
tlum[17]=17;
tlum[18]=18;
tlum[19]=19;
tlum[20]=20;
tlum[21]=21;
tlum[22]=22;
tlum[23]=23;
tlum[24]=24;
tlum[25]=25;
tlum[26]=26;
tlum[27]=27;
tlum[28]=28;
tlum[29]=29;
tlum[30]=30;
tlum[31]=31;
tlum[32]=32;
tlum[33]=33;
tlum[34]=34;
tlum[35]=35;
tlum[36]=36;
tlum[37]=37;
tlum[38]=38;
tlum[39]=39;
tlum[40]=40;
tlum[41]=41;
tlum[42]=42;
tlum[43]=43;
tlum[44]=44;
tlum[45]=45;
tlum[46]=46;
tlum[47]=47;
tlum[48]=48;
tlum[49]=49;
tlum[50]=50;
tlum[51]=51;
tlum[52]=52;
tlum[53]=53;
tlum[54]=54;
tlum[55]=55;
tlum[56]=56;
tlum[57]=57;
tlum[58]=58;
tlum[59]=59;
tlum[60]=60;
tlum[61]=61;
tlum[62]=62;
tlum[63]=63;
tlum[64]=64;
tlum[65]=65;
tlum[66]=66;
tlum[67]=67;
tlum[68]=68;
tlum[69]=69;
tlum[70]=70;
tlum[71]=71;
tlum[72]=72;
tlum[73]=73;
tlum[74]=74;
tlum[75]=75;
tlum[76]=76;
tlum[77]=77;
tlum[78]=78;
tlum[79]=79;
tlum[80]=80;
tlum[81]=81;
tlum[82]=82;
tlum[83]=83;
tlum[84]=84;
tlum[85]=85;
tlum[86]=86;
tlum[87]=87;
tlum[88]=88;
tlum[89]=89;
tlum[90]=90;
tlum[91]=91;
tlum[92]=92;
tlum[93]=93;
tlum[94]=94;
tlum[95]=95;
tlum[96]=96;
tlum[97]=121;
tlum[98]=104;
tlum[99]=101;
tlum[100]=115;
tlum[101]=111;
tlum[102]=99;
tlum[103]=118;
tlum[104]=120;
tlum[105]=100;
tlum[106]=117;
tlum[107]=105;
tlum[108]=103;
tlum[109]=108;
tlum[110]=98;
tlum[111]=107;
tlum[112]=114;
tlum[113]=122;
tlum[114]=116;
tlum[115]=110;
tlum[116]=119;
tlum[117]=106;
tlum[118]=112;
tlum[119]=102;
tlum[120]=109;
tlum[121]=97;
tlum[122]=113;
tlum[123]=123;
tlum[124]=124;
tlum[125]=125;
tlum[126]=126;
tlum[127]=127;
tlum[128]=128;
tlum[129]=129;
tlum[130]=130;
tlum[131]=131;
tlum[132]=132;
tlum[133]=133;
tlum[134]=134;
tlum[135]=135;
tlum[136]=136;
tlum[137]=137;
tlum[138]=138;
tlum[139]=139;
tlum[140]=140;
tlum[141]=141;
tlum[142]=142;
tlum[143]=143;
tlum[144]=144;
tlum[145]=145;
tlum[146]=146;
tlum[147]=147;
tlum[148]=148;
tlum[149]=149;
tlum[150]=150;
tlum[151]=151;
tlum[152]=152;
tlum[153]=153;
tlum[154]=154;
tlum[155]=155;
tlum[156]=156;
tlum[157]=157;
tlum[158]=158;
tlum[159]=159;
tlum[160]=160;
tlum[161]=161;
tlum[162]=162;
tlum[163]=163;
tlum[164]=164;
tlum[165]=165;
    int ts=0;
    tests
    {
        string s;
        while(s.sz==0)
        getline(cin,s);
        FOR(i,s.sz) s[i]=tlum[s[i]];
        printf("Case #%d: ",++ts);
        cout<<s<<"\n";
    }


    return 0;
}
