#include <iostream>
#include <cstdio>
#include <fstream>
#include <cstdlib>
#include <string.h>
using namespace std;
int main()
{ 
  ofstream fout;
  fout.open("A-small.txt");
  
  int T;
  scanf("%d\n", &T);
  
  char a[27] = { 'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q' };
  
  string G;
  int k = 1;
  while( T >= 1 )
  { 
    fout << "Case #" << k << ": ";
    getline(cin, G);
    int n = G.length();
    for( int i = 0; i < n; i++ )
    if( G[i] == ' ' )  { /*cout << " ";*/ fout << ' '; }
    else               { /*cout << a[G[i]-'a'];*/ fout << a[G[i]-'a']; }
    //cout << endl;
    fout << endl;
    k++;
    T--;
   }
  
  fout.close();
  
  //scanf("%d", &T);
  return 0;
}


/*
a -> y
b -> h
c -> e
d -> s
e -> o
f -> c
g -> v
h -> x
i -> d
j -> u
k -> i
l -> g
m -> l
n -> b
o -> k
p -> r
q -> z
r -> t
s -> n
t -> w
u -> j
v -> p
w -> f
x -> m
y -> a
z -> q




Input
3
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv


Output
Case #1: our language is impossible to understand
Case #2: there are twenty six factorial possibilities
Case #3: so it is okay if you want to just give up


30
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv
hello i am the google code jam test data
how are you
aynny iynny aynny iynny aynny iynny aynny iynny aynny iynny aynny iynny aynny iynny aynny ieeeeeeeee
y n f i c w l b k u o m x s e v z p d r j g a t h a q set k oset xa ynfd
schr rkxc tesr aej dksl tkrb xc
eb acyb ympklbr tcpc lessy dbyoc kr jv tkrb rbc vypra ncyp resklbr
dtkwr yd rbc tksi zjkcr yd rbc wepcdr drcyia yd rbc xejsryks
rbkd kd de chfkrksl k bygc re le rbc nyrbpeex
vscjxesejmrpyxkfpedfevkfdkmkfegemfysefeskedkd
eb seeeee lellymep kd bcyici wep rbc epvbysylc
eb xa lei mcrd xyoc ejr
tbeeeeeeeeeeeeeeeeeeeyyyyyyyyy k oset f vmjd vmjd
mcr mkvd ie tbyr bysid ie
ys cac wep ys cac ysi y vklces wep y vklces
w ew rte czjymd w ew esc czjymd esc
wep k ncrtccs rbpcc ysi s w ew k czjymd w ew k xksjd esc vmjd w ew k xksjd rte
wpkcsid iesr mcr wpkcsid mcr dfkcsrkwkf vpelpcdd le nekso
set rbyr aej oset leelmcpcdc vmcydc ie ser jdc kr re byfo ksre ejp dadrcxd
njww rpasiyxcpc ysi yxjxj
aej oset aej tysr re
aej ncrrcp fjr rbc vkqqy ks wejp vkcfcd ncfyjdc kx ser bjslpa csejlb re cyr dkh
k bygc ncdrci wpjkr dvkoc ysi xees set k dbymm ncdr aej rbc lja
lpccrksld fbccdc vevdkfmc rbc sjxncp aej bygc ikymci kd fjppcsrma ejr ew vepofbevd
eb byk kx ks jp fexvjrcp cyrksl aejp fbccqnjplcpd ysi leelmcpcdksl aejp rchrq
tba ie vpelpyxxcpd ymtyad xkh jv bymmetccs ysi fbpkdrxyd
ymm aejp nydc ypc ncmesl re cppep rbc dveesa nypi
set kd rbc djxxcp ew ejp myfo ew ikdfesrcsr


*/
