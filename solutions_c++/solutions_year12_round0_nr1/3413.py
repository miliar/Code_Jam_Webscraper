#include <iostream>
#include <fstream>
#include <cstring>
#include <queue>

int main()
{
    int T;
    int count = 0;
    char a[20000];

    std::ofstream fout("A-small-attempt1.out");
    std::ifstream fin("A.in");

	std::queue<char*> S;

	std::cin>>T;
    std::cin.ignore();

    for (int i=0; i<T; i++)
    {
        fin.getline(a,20000);
		char* b = new char[strlen(a)+1];
		strcpy(b,a);
        S.push(b);
    }
    fin.close();
	while (!S.empty())
	{
		++count;
		for (int i=0; i<strlen(S.front()); i++)
		{
			switch(S.front()[i])
			{
			case 'a': S.front()[i]='y'; break;
			case 'b': S.front()[i]='h'; break;
			case 'c': S.front()[i]='e'; break;
			case 'd': S.front()[i]='s'; break;
			case 'e': S.front()[i]='o'; break;
			case 'f': S.front()[i]='c'; break;
			case 'g': S.front()[i]='v'; break;
			case 'h': S.front()[i]='x'; break;
			case 'i': S.front()[i]='d'; break;
			case 'j': S.front()[i]='u'; break;
			case 'k': S.front()[i]='i'; break;
			case 'l': S.front()[i]='g'; break;
			case 'm': S.front()[i]='l'; break;
			case 'n': S.front()[i]='b'; break;
			case 'o': S.front()[i]='k'; break;
			case 'p': S.front()[i]='r'; break;
			case 'q': S.front()[i]='z'; break;
			case 'r': S.front()[i]='t'; break;
			case 's': S.front()[i]='n'; break;
			case 't': S.front()[i]='w'; break;
			case 'u': S.front()[i]='j'; break;
			case 'v': S.front()[i]='p'; break;
			case 'w': S.front()[i]='f'; break;
			case 'x': S.front()[i]='m'; break;
			case 'y': S.front()[i]='a'; break;
			case 'z': S.front()[i]='q'; break;
			}
		}
		fout<<"Case #"<<count<<": "<<S.front()<<"\n";
		S.pop();
	}

    return 0;
}

/*
30
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv
hello i am the google code jam test data
how are you
aynny iynny aynny iynny aynny iynny aynny iynny aynny iynny aynny iynny aynny iynny aynny ieeeeeeeee
y n f i c w l b k u o m x s e v z p d r j g a t h a q set k oset xa ynfd
schr rkxc tesr aej dksl tkrb xc
wpkcsid iesr mcr wpkcsid mcr dfkcsrkwkf vpelpcdd le nekso
w ew rte czjymd w ew esc czjymd esc
wep k ncrtccs rbpcc ysi s w ew k czjymd w ew k xksjd esc vmjd w ew k xksjd rte
pklbr k wepler bcpc ks rbc dryrcd aej fymm kr y dyjdylc ks rbc xejrb
k bygc ncdrci wpjkr dvkoc ysi xees set k dbymm ncdr aej rbc lja
set rbyr aej oset leelmcpcdc vmcydc ie ser jdc kr re byfo ksre ejp dadrcxd
na rbc vpkfoksl ew xa rbjxnd dexcrbksl tkfoci rbkd tya fexcd
cyfb ew jd byd bkd ets dvcfkym lkwr ysi aej oset rbkd tyd xcysr re nc rpjc
ysi kw aej iesr jsicpcdrkxyrc xc k tesr jsicpcdrkxyrc aej
ymm aejp nydc ypc ncmesl re cppep rbc dveesa nypi
kx fexxysicp dbcvypi ysi rbkd kd xa wygepkrc vpenmcx es rbc leelmc feic uyx
wep rbedc tbe dvcyo ks y resljc ie ser dvcyo re erbcp vcevmc
seneia jsicpdrysid rbcx dksfc rbca ypc dvcyoksl xadrcpkcd ks rbc dvkpkr
tbeeeeeeeeeeeeeeeeeeeyyyyyyyyy k oset f vmjd vmjd
mcr mkvd ie tbyr bysid ie
rbkd bcpc kd ljsveticp yfrkgyrci rtcsra dcgcs fymkncp wjmm yjre se okfonyfo sykmrbpetksl xyabcx
aej tysr dcmm rbksld yr xc neksl qeeex
ys cac wep ys cac ysi y vklces wep y vklces
vscjxesejmrpyxkfpedfevkfdkmkfegemfysefeskedkd
lpccrksld fbccdc vevdkfmc rbc sjxncp aej bygc ikymci kd fjppcsrma ejr ew vepofbevd
eb seeeee lellymep kd bcyici wep rbc epvbysylc
eb xa lei mcrd xyoc ejr

*/
