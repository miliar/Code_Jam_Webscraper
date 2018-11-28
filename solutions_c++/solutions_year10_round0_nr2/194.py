#include <iostream>
#include <vector>
#include <list>
#include <algorithm>

using namespace std;

const int max_column=51;

class CNumber
{
public:
  char exp[max_column];
  int column;

  void initialize()
  {
    column = 0;
    for(int i=0; i<max_column; i++){
      exp[i]=0;
    }
  }
  CNumber()
  {
    initialize();
  }
  CNumber(const CNumber& obj)
  {
    column = obj.column;
    for(int i=0; i<max_column; i++){
      exp[i]=obj.exp[i];
    }
  }
  CNumber(string arg){
    initialize();

    column = arg.size();
    for(int i=0; i<column; i++){
      exp[column-1-i] = arg[i] - '0';
    }

    normalize();
  }

  string show() const
  {
    string rval="";

    if(column == 0)return "0";

    for(int i=0; i<column; i++){
      rval = (char)(exp[i]+'0') + rval;
    }

    return rval;
  }

  bool operator>(const CNumber& obj) const
  {
    return this->cmp(obj) > 0;
  }
  bool operator==(const CNumber& obj) const
  {
    return this->cmp(obj) == 0;
  }
  int cmp(const CNumber& obj) const
  {
    if(column > obj.column)return 1;
    if(column < obj.column)return -1;
    for(int i=column-1; i>=0; i--){
      if(exp[i] > obj.exp[i])return 1;
      if(exp[i] < obj.exp[i])return -1;
    }
    return 0;
  }
  CNumber operator-(const CNumber& obj) const
  {
    CNumber rval;

    if(obj > *this)return obj - *this;

    for(int i=0; i<column; i++){
      rval.exp[i] = exp[i] - obj.exp[i];
    }
    rval.normalize();

    return rval;
  }
  void normalize(void)
  {
    column = -1;

    for(int i=0; i<max_column; i++){
      if(exp[i] < 0){
	exp[i]+=10;
	--exp[i+1];
      }
      if(exp[i]>0)column=i;
    }
    ++column;
  }
};

void minus_eager(CNumber& sec, CNumber& div)
{
  int mult;
  int c = sec.cmp(div);

  if(c < 0)return;

  mult = sec.column - div.column;
  for(int i=div.column-1; i>=0; i--){
    if(sec.exp[i+mult] > div.exp[i])break;
    if(sec.exp[i+mult] < div.exp[i]){
      --mult;
      break;
    }
  }

  for(int i=0; i<div.column; i++){
    sec.exp[i+mult] -= div.exp[i];
  }
  sec.normalize();

  minus_eager(sec, div);
}

void gojo(CNumber& obj1, CNumber&obj2)
{
  int c;

  if(obj1.column == 0){
    obj1 = obj2;
    return;
  }
  if(obj2.column == 0){
    obj2 = obj1;
    return;
  }

  c = obj1.cmp(obj2); 
  if(c == 0)return;
  if(c < 0){
    gojo(obj2, obj1);
    return;
  }

  // obj1 > obj2
  minus_eager(obj1, obj2);

  gojo(obj2, obj1);
}

void solve(void)
{
  list<CNumber> num_list;
  list<CNumber> div_list;
  CNumber kouyaku;
  int N;

  num_list.clear();
  div_list.clear();

  cin >> N;

  for(int i=0; i<N; i++){
    string numstr;

    cin >> numstr;
    num_list.push_back(CNumber(numstr));
  }

  list<CNumber>::iterator it=num_list.begin();
  for(++it; it != num_list.end(); ++it){
    div_list.push_back(*num_list.begin() - *it);
  }

  // set 0
  kouyaku.initialize();

  for(list<CNumber>::iterator it = div_list.begin();
      it != div_list.end(); ++it){
    gojo(kouyaku, *it);
  }

  CNumber t = *num_list.begin();

  minus_eager(t, kouyaku);

  if(t.column == 0){
    cout << "0\n";
  }
  else{
    cout << (kouyaku - t).show() << "\n";
  }
}

int main()
{
  int C;

  cin >> C;

  for(int i=0; i<C; i++){
    cout << "Case #" << (i+1) << ": ";
    solve();
  }
}
