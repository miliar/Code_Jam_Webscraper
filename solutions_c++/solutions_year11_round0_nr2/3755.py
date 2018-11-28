#include <stdio.h>
#include <vector>
#include <iostream>
#include <map>
#include <set>

using namespace std;

typedef pair< unsigned, unsigned > btn_t;

typedef vector< pair<unsigned, unsigned > > sequence_t;

typedef map< string, char > base_t;
typedef map<char, char> opposed_t;

//#define KDEBUG
#ifdef KDEBUG
#define DPRINT(x) printf("%s", x )
#define VAL(x) cout << "value " << #x << " = " << x << endl;
#else
#define DPRINT(x) ;
#define VAL(x) ;
#endif


void solve( unsigned case_no, base_t &base, opposed_t &opp, string &seq )
{
   //VAL(seq.size());
   VAL(seq);
   string result;
   char previous;
   map<char,int>::iterator mit;
   map<char,int> mchar;

   base_t::iterator bit;
   opposed_t::iterator oit;

   for(int i = 0; i< seq.size();++i)
   {
	   VAL(result);
	   if (result.size() == 0)
	   {
	   result.push_back(seq[i]);
	   mchar[seq[i]] ++;
	   previous = seq[i];
	   continue;
	   }
	   
	   string px;
	   px.push_back(seq[i]);
	   px.push_back(previous);
	   VAL(px);
	   VAL(base.size());
/*	   for (bit = base.begin(); bit!=base.end(); ++bit)
	   {
		   VAL( (*bit).first);
		   VAL( (*bit).second);
	   }
*/
	   bit = base.find(px);
	   if (bit!= base.end())
	   {
		   //cout << "WE hav found something in the map " << (*bit).second <<endl;
		   DPRINT("REPLACING RESULT WIHT\n");
		   VAL((*bit).second);
		   result.resize(result.size()-1);
		   result.push_back( (*bit).second );
		   previous = (*bit).second;
		   mchar[px[0]]--;
		   mchar[px[1]]--;
		   continue;
	   }
	   else // we did not found base element
	   {
		   oit = opp.find(seq[i]);
		   if (oit != opp.end() )
		   {
			   mit = mchar.find((*oit).second);
			   if (mit != mchar.end())
			   {
				   if ( (*mit).second > 0)
				   {
				   DPRINT("OPPOSED ELEMENT FOUND\n");
				   VAL(seq[i]);
				   VAL((*mit).first);
				   mchar.clear();
				   result.clear();
				   continue;
				   }

			   }

		   }
	   }


	   
	   result.push_back(seq[i]);
	   previous = seq[i];
	   mchar[seq[i]] ++;
   }


   printf("Case #%d: [", case_no);
   for (int i = 0;i < result.size(); ++i) 
   {
	   printf("%c", result[i] );
	   if (i < result.size() - 1 ) printf(", ");
   }
   printf("]\n");
}

int main()
{
	unsigned _tc;
	scanf("%d", &_tc );
	for (unsigned _tc_it= 0; _tc_it < _tc; ++_tc_it)
	{
		base_t base;
		opposed_t opposed;
		string seq;

		int c_base, c_opp;
//		cin >> c_base;
		scanf("%d", &c_base);
		VAL(c_base);
	
		for (int i = 0;i < c_base; ++i)
		{
			string basex;
			cin >> basex;
			string p1, p2;
			p1.resize(2);
			p2.resize(2);
			p1[0] = basex[0];
			p1[1] = basex[1];
			p2[0] = basex[1];
			p2[1] = basex[0];

			base[p1] = basex[2];
			base[p2] = basex[2];
//			cout << basex << endl;
		}
//		cin >> c_opp;
		scanf("%d", &c_opp);
		
//		cout << c_opp << endl;
		VAL(c_opp);
		for (int i = 0;i < c_opp; ++i)
		{
			string oppx;
			cin >> oppx;
			opposed[oppx[0]] = oppx[1];
			opposed[oppx[1]] = oppx[0];
	//		cout << oppx << endl;
		}
		int s_size;
		cin >> s_size;

		cin >> seq;
//		cout << "SEQ = " << seq << endl;
		
		solve( _tc_it + 1, base, opposed, seq);
	}
};
