#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <set> 
#include <vector>
#include <sstream>
#include <stdlib.h>
#include <list>
using namespace std;
string plist(list<int>& l)
{
  list<int>::iterator itr = l.begin();
  string s = "";
  for (;itr != l.end(); itr ++){
    s += char(*itr + int('0'));
  }
  return s;
}
void normList(list<int>& l)
{
  list<int>::iterator itr = l.begin();
  while(itr != l.end() && *itr == 0) {
    itr = l.erase(itr); 
  }
  if (itr == l.end())
    l.push_back(0);
}
bool largeBigger(list<int>& lhs, list<int>& rhs)
{
  if (lhs.size() > rhs.size()) return true;
  else if (lhs.size() < rhs.size()) return false;
  else {
    list<int>::iterator itr1 = lhs.begin();
    list<int>::iterator itr2 = rhs.begin();
    for (;itr1 != lhs.end(); itr1++,itr2++) {
      if (*itr1 > * itr2) return true;
      else if (*itr1 < * itr2) return false;
    }
  }
  return false;
}
bool largeEqual(list<int>& lhs, list<int>& rhs)
{
  if (lhs.size() != rhs.size()) return false;
  else {
    list<int>::iterator itr1 = lhs.begin();
    list<int>::iterator itr2 = rhs.begin();
    for (;itr1 != lhs.end(); itr1++,itr2++) {
      if (*itr1 != * itr2) return false;
    }
  }
  return true;
}
list<int> largeMinus(list<int>& lhs, list<int>& rhs)
{
  //make sure lhs > rhs =.=
  //cout<<"minus "<<plist(lhs)<<" "<<plist(rhs)<<endl;
  list<int>::reverse_iterator itr1 = lhs.rbegin();
  list<int>::reverse_iterator itr2 = rhs.rbegin();
  list<int> rtn;
  int borrow = 0;
  for (;itr1 != lhs.rend(); itr1++) {
    if (itr2 != rhs.rend()) {
      int l = *itr1 - borrow;
      int r = *itr2;
      if (l < r) {
	borrow = 1;
	rtn.push_front(10 + l - r);
      }
      else {
	borrow = 0;
	rtn.push_front(l - r);
      }
      itr2 ++;
    }
    else {
      if (borrow == 1) {
	if (*itr1 < borrow) {
      	  rtn.push_front(*itr1 + 9);
	}
	else {
	  rtn.push_front(*itr1 - borrow);
 	  borrow = 0;
	}
      }
      else {
	rtn.push_front(*itr1);
      }
    }
  }
  normList(rtn);
  return rtn;
}
list<int> largeMod(list<int>& lhs, list<int>& rhs)
{
  //cout<<"mod "<<plist(lhs)<<" "<<plist(rhs)<<endl;
  if (largeEqual(lhs,rhs)) {
    list<int> rtn;
    rtn.push_back(0);
    return rtn;
  }
  else if (largeBigger(rhs,lhs)) {
    list<int> rtn = lhs;
    return rtn;
  }
  else if (rhs.size() == 1 && rhs.front() == 1) {
    list<int> rtn;
    rtn.push_back(0);
    return rtn;
  }
  else {
    list<int> l,r;
    l = lhs;
    r = rhs;
    if (r.size() == 1 && r.front() == 1) {
      list<int> rtn;
      rtn.push_back(0);
      return rtn;
    }
    while(largeBigger(l,r) || largeEqual(l,r)) {
      l = largeMinus(l,r);
    }
    return l;
  }
}
list<int> largeGCD(list<int>& lhs, list<int>& rhs)
{
  //cout<<"mod "<<plist(lhs)<<" "<<plist(rhs)<<endl;
  if (largeEqual(lhs,rhs)) {
    list<int> rtn = lhs;
    return rtn;
  }
  list<int> l,r;
  l = lhs;
  r = rhs;
  if (r.size() == 1 && r.front() == 1) {
    return r;
  }
  else if (l.size() == 1 && l.front() == 0) {
    cout<<"ERROR\n";
  } 
  else if (r.size() == 1 && r.front() == 0) {
    cout<<"ERROR\n";
  }
  else {
    while(largeBigger(l,r)) {
      l = largeMinus(l,r);
    }
    return largeGCD(r,l);
  }
}
int main()
{
  ifstream ins("testcase");
  ofstream ous("result");
  string line;
  getline(ins,line);
  int caseNum = atoi(line.c_str());
  for (int i = 0 ; i < caseNum; i++) {
    getline(ins,line);
    stringstream ss(line);
    int n;
    ss >> n;
    list<int> eventVct[n];
    list<int> minusVct[n - 1];
    set<string> eventSet;
    for (int j = 0; j < n; j ++){
      string largeNum;
      ss>>largeNum;
      eventSet.insert(largeNum);
    }
    n = 0;
    set<string>::iterator iitr = eventSet.begin();
    cout<<"set:";
    for (; iitr != eventSet.end(); iitr ++, n ++){
      string largeNum = *iitr;
      cout<<largeNum<<" ";
      for (int k = 0; k < largeNum.size(); k ++) {
	eventVct[n].push_back(largeNum[k] - int('0'));
      }
    }
    list<int> *min = &eventVct[0];
    cout<<"\nminus:";
    for (int j = 0; j < n - 1; j ++) {
      if (largeBigger(eventVct[j],eventVct[j+1])) 
	minusVct[j] = largeMinus(eventVct[j],eventVct[j+1]); 
      else
	minusVct[j] = largeMinus(eventVct[j+1],eventVct[j]);
      if (largeBigger(*min,eventVct[j + 1]))
	*min = eventVct[j + 1];
      cout<<plist(minusVct[j])<<" ";
    }
    cout<<endl;
    list<int> t = minusVct[0];
    if (n > 2) {
      list<int> gcdResult = minusVct[0];
      //cout<<plist(gcdResult)<<" ";
      for(int j = 1; j < n - 1; j ++) {
        gcdResult = largeGCD(gcdResult,minusVct[j]);
	//cout<<plist(gcdResult)<<" ";
	if (gcdResult.size() == 1 && gcdResult.front() == 1)
	  break;
      }
      cout<<"gcd:"<<plist(gcdResult)<<endl;
      if (gcdResult.size() == 1 && gcdResult.front() == 1) {
	t.clear();
	t.push_back(0);
      }
      else {
        cout<<"mod "<<plist(*min)<<" "<<plist(gcdResult)<<endl;
        list<int> tmp = largeMod(*min,gcdResult);
        cout<<"return "<<plist(tmp)<<endl;
	if (tmp.size() == 1 && tmp.front() == 0) {
	  t.clear();
	  t.push_back(0);
	}
        else t = largeMinus(gcdResult,tmp);
        cout<<"return "<<plist(t)<<endl;
      }
    }
    else if (n == 2){
      //cout<<"compare "<<plist(tmp1)<<" "<<plist(tmp2)<<endl;
      if (t.size() == 1 && t.front() == 1) {
	t.front() = 0;
      }
      else {
	cout<<"mod "<<plist(*min)<<" "<<plist(t)<<endl;
	list<int> tmp = largeMod(*min,t);
	cout<<"return "<<plist(tmp)<<endl;
	if (tmp.size() == 1 && tmp.front() == 0) {
	  t.clear();
	  t.push_back(0);
        }
	else t = largeMinus(t,tmp);
	cout<<"result "<<plist(t)<<endl;
      }
    }
    else {
      t.clear();
      t.push_back(0);
    }
    cout<<"Case #"<< i + 1 << ": "<<plist(t)<<endl;
    ous<<"Case #"<< i + 1 << ": "<<plist(t)<<endl;
    //getchar();
  }
}