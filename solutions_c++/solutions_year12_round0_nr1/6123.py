#include<iostream>
#include<fstream>
using namespace std;
int main()
{       
          ofstream fout;
          fout.open("ans.txt");
          int t,p=0;
          cin>>t;
          getchar();
          while(t--)
          {  p++;
           char ch[10000];
           char a[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
           gets(ch);
           int l=strlen(ch);
           cout<<l<<endl;
           for(int i=0;i<l;i++)
           {
             if(ch[i]!=' ')
             {
              ch[i]=a[ch[i]-'a'];
              }
              }
              if(t!=0)
              fout<<"Case #"<<p<<": "<<ch<<endl;
              else
               fout<<"Case #"<<p<<": "<<ch;         
           }
           //system("pause");
           return 0;
           }
           
/*
5
gh
kl
30
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv
hello i am the google code jam test data
how are you
aynny iynny aynny iynny aynny iynny aynny iynny aynny iynny aynny iynny aynny iynny aynny ieeeeeeeee
y n f i c w l b k u o m x s e v z p d r j g a t h a q set k oset xa ynfd
schr rkxc tesr aej dksl tkrb xc
na rbc vpkfoksl ew xa rbjxnd dexcrbksl tkfoci rbkd tya fexcd
bet ypc aej bemiksl jv ncfyjdc kx y veryre
eb seeeee lellymep kd bcyici wep rbc epvbysylc
eb xa lei mcrd xyoc ejr
aej ncrrcp fjr rbc vkqqy ks wejp vkcfcd ncfyjdc kx ser bjslpa csejlb re cyr dkh
rpysdmyrksl rchr kd ser leped drpcslrb
drpcslrb kd leped drpcslrb
wpkcsid iesr mcr wpkcsid mcr dfkcsrkwkf vpelpcdd le nekso
eb byk kx ks jp fexvjrcp cyrksl aejp fbccqnjplcpd ysi leelmcpcdksl aejp rchrq
tba ie vpelpyxxcpd ymtyad xkh jv bymmetccs ysi fbpkdrxyd
set rbyr aej oset leelmcpcdc vmcydc ie ser jdc kr re byfo ksre ejp dadrcxd
ys cac wep ys cac ysi y vklces wep y vklces
pklbr k wepler bcpc ks rbc dryrcd aej fymm kr y dyjdylc ks rbc xejrb
njww rpasiyxcpc ysi yxjxj
aej oset aej tysr re
rbkd kd de chfkrksl k bygc re le rbc nyrbpeex
ymm aejp nydc ypc ncmesl re cppep rbc dveesa nypi
eb acyb ympklbr tcpc lessy dbyoc kr jv tkrb rbc vypra ncyp resklbr
cyfb ew jd byd bkd ets dvcfkym lkwr ysi aej oset rbkd tyd xcysr re nc rpjc
ysi kw aej iesr jsicpcdrkxyrc xc k tesr jsicpcdrkxyrc aej
k bygc ncdrci wpjkr dvkoc ysi xees set k dbymm ncdr aej rbc lja
ks y tepmi ew ikpctemgcd ysi mkesd dexcrkxcd rbc pypcdr fpcyrjpc kd y wpkcsi */
