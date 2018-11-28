#include <iostream>
#include <algorithm>
#include <iomanip>
#include <sstream>
#include <queue>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <cstdlib>
#include <cmath>
#include<fstream>
using namespace std;

typedef vector <int> vi;
typedef vector<vi> vvi;
typedef vector <string> vs;
typedef vector<vs> vvs;
typedef long long i64;
typedef unsigned long long u64;
typedef pair<int,int> pii;

istringstream din;
ostringstream dout;


ifstream fin("B-large.in");
ofstream fout("B-large.out");
/*
ifstream fin("temp.in");
ofstream fout("temp.out");
*/
struct _h
{
  bool dir;// false: A->B , true: B->A
  int ih,im;
  int eh,em;
};
struct _t
{
  bool pos; // false: at A, true: at B
  int h,m;
};

int N,T,NA,NB;
int ra,rb;

vector<_t> avl;

vector<_h> vh;
vector<_h> vha;
vector<_h> vhb;



_t makeT(int h,int m,bool pos)
{
  _t t;
  t.pos = pos;
  t.m = (m + T)%60;
  t.h = (h + (m+T)/60);
  
  return t;
}

int find_avl(int pos, int h, int m)
{
  if (avl.size() == 0) return -1;
  for (int i = 0;i < avl.size();i++) {
    if (pos != avl[i].pos) continue;
    
    if (avl[i].h < h) return i;
    if (avl[i].h == h && avl[i].m <= m) return i;
  }
  return -1;
}

bool comp0(_h a,_h b){
  if (a.ih == b.ih)
    return a.im < b.im;
  return a.ih < b.ih;
}

void init()
{
  avl.clear();vh.clear();vha.clear();vhb.clear();
}

string update(string str)
{
  for (int i = 0;i < str.length();i++)
    str[i] = (str[i] == ':' ? ' ':str[i]);
  return str;
}

void resolve()
{
  //cerr << endl << endl;
  int sz = vh.size();
  ra = rb = 0;
  for (int i = 0;i < sz;i++) {
    int pos = vh[i].dir;
    int avl_id = find_avl(pos,vh[i].ih,vh[i].im);

    //cerr << "req: " << (pos == false ? "A "  : "B " );
    //cerr << vh[i].ih << ":" << vh[i].im << endl;
    
    if (avl_id == -1) { // no avl
      if (pos == false) { // at A
	ra++;
	avl.push_back(makeT(vh[i].eh,vh[i].em,true));
      }else { // at B
	rb++;
	avl.push_back(makeT(vh[i].eh,vh[i].em,false));
      }
    }else {
      // update the found avl
      avl[avl_id] = makeT(vh[i].eh,vh[i].em,!pos);
    }
    
    //cerr << (avl_id == -1 ? "n " : "y ") <<  "ra = " << ra << " rb = " << rb << endl;
  }
}

int main()
{
  string str;
  int ih,im,eh,em;


  fin >> N;
  for (int i = 0;i < N;i++) {
    init();

    fin >> T >> NA >> NB;
    getline(fin,str);
    for (int j = 0;j < NA;j++) {
      getline(fin,str);
      str = update(str);
      din.clear();din.str(str);
      _h hh;
      hh.dir = false;
      din >> hh.ih >> hh.im >> hh.eh >> hh.em;
      //cerr << hh.ih << ":" << hh.im << " " << hh.eh << ":" << hh.em << endl;
      vh.push_back(hh);
      vha.push_back(hh);
    }
    for (int j = 0;j < NB;j++) {
      getline(fin,str);
      str = update(str);
      din.clear();din.str(str);
      _h hh;
      hh.dir = true;
      din >> hh.ih >> hh.im >> hh.eh >> hh.em;
      //cerr << hh.ih << ":" << hh.im << " " << hh.eh << ":" << hh.em << endl;
      vh.push_back(hh);
      vhb.push_back(hh);
    }

    if (NA == 0 || NB == 0) {
      if (NA == NB) ra = rb = 0;
      else {
	if (NA == 0) {
	  ra = 0;rb = NB;
	}else {
	  rb = 0;ra = NA;
	}
      }
    }
    else {
      sort(vh.begin(),vh.end(),comp0);
      sort(vha.begin(),vha.end(),comp0);
      sort(vhb.begin(),vhb.end(),comp0);
      
      /*
      for (int i = 0;i < vh.size();i++) {
	cerr << vh[i].ih << ":" << vh[i].im << endl;
      }
      */
      resolve();
    }
    
    fout << "Case #" << (i+1) << ": " << ra << " " << rb << endl;
  }

  fin.close();fout.close();
  return 0;
}

