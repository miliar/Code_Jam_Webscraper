#include <cassert>
#include <cstdio>
#include <iostream>


char tr[26]={};


void wtf(char const *e, char const *d)
{
	while(*e && *d)
	{
		char ce=*e++;
		char cd=*d++;
		bool both_letters='a'<=ce && ce<='z' && 'a'<=cd && cd<='z';
		if(both_letters)
		{
			int ie=ce-'a';
			assert(0<=ie && ie<26 && (tr[ie]==0 || tr[ie]==cd));
			tr[ie]=cd;
		}
		else assert(ce==' ' && cd==' ');
	}
	assert(!*e && !*d);
}


int main()
{
	wtf("yeqz", "aozq");
	wtf("ejp mysljylc kd kxveddknmc re jsicpdrysi", "our language is impossible to understand");
	wtf("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "there are twenty six factorial possibilities");
	wtf("de kr kd eoya kw aej tysr re ujdr lkgc jv", "so it is okay if you want to just give up");
	//for(size_t i=0; i<26; ++i)
	//	std::cout << char('a'+i) << " " << tr[i] << std::endl;
	size_t T=0;
	scanf("%zu\n", &T);
	for(size_t t=1; t<=T; ++t)
	{
		size_t const G=100;
		char e[G+1], d[G+1];
		scanf("%[a-z ]\n", e);
		size_t g=0;
		for(; g<G && e[g]; ++g)
		{
			char ce=e[g];
			if(ce==' ')
				d[g]=' ';
			else
			{
				size_t ie=ce-'a';
				assert(ie<26);
				d[g]=ie<26?tr[ie]:'_';
			}
		}
		d[g]=0;
		printf("Case #%zu: %s\n", t, d); 
	}
	return 0;
}

