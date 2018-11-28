#include "scc/cj.h"		// http://github.com/lvv/scc


int main() {
	size_t tt(in);  NL;

	vchar tab(256,0);
	vstr S, G;

S << "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
G << "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
	S << " aozq";
	G << " yeqz";

	while (!S.empty()) {
		while(!S++.empty()) {
			tab[S ++ ++] = G ++ ++ ;
			S ++ --;
			G ++ --;
		}
		S --;
		G --;
	};
								/*for (char c='a';  c<='z';  c++)  {
									_ c; 
									if (tab[c]) 	__ "\t->  ", tab[c];
									else		__ "";	
								}*/


	std::filebuf fb;
	fb.open ("/usr/share/dict/words",std::ios::in);
	istream words(&fb);
	set<str> dic;
	str w;
	while (getline(words, w))  dic << w;
	dic << "okay" << "porkchops" << "textz" << "pizza" /*<< "zooom"*/ << "cheezburgers" << "cheezburger" << "boink";
	auto it = dic.find("enow");  dic.erase(it);
	it = dic.find("thane");  dic.erase(it);
	it = dic.find("lace");  dic.erase(it);

		

	str s, l;

	for(size_t t=1;  t<=tt;  t++)  {
		cout << "Case #" <<  t << ": ";
		getline(cin,l); 
		istringstream iss (l);
		iss >> s; 
		do {
			w.clear();
			for(char c: s)  w <<  (tab[c] ? tab[c] : c);

			const char FROM[]="eq";
			const char TO[]="kz";
			str w0 = w;
	goto out;

			for (size_t i=0; i<2; i++) {

				char from=FROM[i];
				char to=TO[i];
				w = w0;

				if (w.size() > 2  &&  dic.find(w) == -dic) {
					bool all = false;
					forall:
						auto e = +w;
						while ((e = find(e, -w, from)) != -w) {
							*e = to;
							if (dic.find(w) != -dic) {
											//			__ "\nrepl:\t", w;
								goto out;
							}

							if (!all) *e = from;
							++e;
						}

					if (!all) {
						all=true;
						goto forall;
					}

				}
				w = w0;
			}
			out:
			cout << w;
		} while (iss >> s && cout << " ");
		cout << endl;
	}
}
