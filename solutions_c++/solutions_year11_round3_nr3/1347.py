#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<cmath>
using namespace std;
typedef long long LLI;
typedef long double LD;

LLI nod(LLI a, LLI b) {
  while (a!=0 && b!=0) {
    if (b>a) 
      b%=a;
    else
      a%=b;
  }
  return a==0?b:a;
}

LLI group_nod(const vector<LLI> &A, const int from, const int to) {
  if (from==to) return A[from];
  LLI res = nod(A[from], A[from+1]);
  for (int i=from+2;i<=to;i++) {
    res = nod(res, A[i]);
  }
  return res;
}

LLI div_group(const vector<LLI> &A, const int from, const int to, LLI l ,LLI r) {
  LLI res = A[from];

  for (int i=from+1;i<=to;i++) {
    res*=A[i]/nod(res, A[i]);
    if (res>r) return 0;
  }
  return res;
}

LLI validate(const LLI must_be_divided, const LLI must_divide, const LLI l, const LLI r) {
  if (must_divide==0) return -1;
  if (must_be_divided%must_divide != 0) return -1;
  if (l%must_divide == 0 && l <= must_be_divided) return l;
  LLI Min = ((LLI)(l/must_divide) + 1)*must_divide;
  if (Min > r || Min > must_be_divided) return -1;
  return Min;
}

int main() {
  int NT;
  cin >> NT;
  for (int test=1;test<=NT;test++) {
    LLI n,l,r;
    cin >> n >> l >> r;
    vector<LLI> A(n);
    for (int i=0;i<n;i++)
      cin >> A[i];
    sort(A.begin(), A.end());
    /*    LLI res;
    res = validate(group_nod(A, 0, n-1), 1, l, r);
    LLI tmp = div_group(A, 0, n-1, l, r);
    LLI cur_res;
    if (tmp!=0)
      cur_res = validate((LLI)((LLI)(r/tmp)*(LLI)tmp), tmp, l, r);
    else 
      cur_res = -1;
    if (res==-1 || cur_res < res && cur_res!=-1) res = cur_res;
    for (int i=0;i<n-1;i++) {
      //            cout << "cur_res=" << cur_res << endl;
      cur_res = validate(group_nod(A, i+1, n-1), div_group(A, 0, i, l, r), l, r);
      if (res == -1 || cur_res < res && cur_res!=-1) res = cur_res;
    }
    cout << "Case #" << test << ": ";
    if (res == -1) 
      cout << "NO" << endl;
    else
    cout << res << endl;*/
    LLI res = -1;
    for (LLI i=l;i<=r;i++)
      {
	bool is_valid = true;
	for (int j=0;j<n;j++)
	  if (i%A[j]==0 || A[j]%i==0) {
	    ;
	  } else {
	    is_valid = false;
	    break;
	  }
	if (is_valid) {
	  res = i;
	  break;
	}
      }
    cout << "Case #" << test << ": ";
    if (res==-1) cout << "NO" << endl; else cout << res << endl;
  }
  return 0;
}
