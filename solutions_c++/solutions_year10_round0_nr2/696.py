#include <iostream>
#include <vector>

using namespace std;

typedef long long hugeint; 

const int Base = 1000000000; 
const int Capacity = 200; 

struct xnum { 
    int Len; 
    int Data[Capacity]; 
    xnum() : Len(0) {} 
    xnum(const xnum& V) : Len(V.Len) { memcpy(Data, V.Data, Len * sizeof *Data); } 
    xnum(int V) : Len(0) { for (; V > 0; V /= Base) Data[Len++] = V % Base; } 
    xnum& operator=(const xnum& V) { Len = V.Len; memcpy(Data, V.Data, Len * sizeof *Data); return *this; } 
    int& operator[](int Index) { return Data[Index]; } 
    int operator[](int Index) const { return Data[Index]; } 
}; 


int compare(const xnum& A, const xnum& B) { 
    int I; 
    if (A.Len != B.Len) return A.Len > B.Len ? 1 : -1; 
    for (I = A.Len - 1; I >= 0 && A[I] == B[I]; I--); 
    if (I < 0) return 0; 
    return A[I] > B[I] ? 1 : -1; 
} 

bool operator == (const xnum& A, const xnum& B) { 
	return compare(A, B) == 0;
}

bool operator < (const xnum& A, const xnum& B) { 
	return compare(A, B) < 0;
}

bool operator > (const xnum& A, const xnum& B) { 
	return compare(A, B) > 0;
}

bool operator != (const xnum& A, const xnum& B) { 
	return compare(A, B) != 0;
}

xnum operator+(const xnum& A, const xnum& B) { 
    xnum R; 
    int I; 
    int Carry = 0; 
    for (I = 0; I < A.Len || I < B.Len || Carry > 0; I++) { 
        if (I < A.Len) Carry += A[I]; 
        if (I < B.Len) Carry += B[I]; 
        R[I] = Carry % Base; 
        Carry /= Base; 
    } 
    R.Len = I; 
    return R; 
} 

xnum operator-(const xnum& A, const xnum& B) { 
    xnum R; 
    int Carry = 0; 
    R.Len = A.Len; 
    int I; 
    for (I = 0; I < R.Len; I++) { 
        R[I] = A[I] - Carry; 
        if (I < B.Len) R[I] -= B[I]; 
        if (R[I] < 0) Carry = 1, R[I] += Base; 
        else Carry = 0; 
    } 
    while (R.Len > 0 && R[R.Len - 1] == 0) R.Len--; 
    return R; 
} 

xnum operator*(const xnum& A, const int B) { 
    int I; 
    if (B == 0) return 0; 
    xnum R; 
    hugeint Carry = 0; 
    for (I = 0; I < A.Len || Carry > 0; I++) { 
        if (I < A.Len) Carry += hugeint(A[I]) * B; 
        R[I] = Carry % Base; 
        Carry /= Base; 
    } 
    R.Len = I; 
    return R; 
} 

xnum operator*(const xnum& A, const xnum& B) { 
    int I; 
    if (B.Len == 0) return 0; 
    xnum R; 
    for (I = 0; I < A.Len; I++) { 
        hugeint Carry = 0; 
        for (int J = 0; J < B.Len || Carry > 0; J++) { 
            if (J < B.Len) Carry += hugeint(A[I]) * B[J]; 
            if (I + J < R.Len) Carry += R[I + J]; 
            if (I + J >= R.Len) R[R.Len++] = Carry % Base; 
            else R[I + J] = Carry % Base; 
            Carry /= Base; 
        } 
    } 
    return R; 
} 

xnum operator/(const xnum& A, const int B) { 
    xnum R; 
    int I; 
    hugeint C = 0; 
    for (I = A.Len - 1; I >= 0; I--) { 
        C = C * Base + A[I]; 
        R[I] = C / B; 
        C %= B; 
    } 
    R.Len = A.Len; 
    while (R.Len > 0 && R[R.Len - 1] == 0) R.Len--; 
    return R; 
} 

int operator%(const xnum& A, const int B) { 
    xnum R; 
    int I; 
    hugeint C = 0; 
    for (I = A.Len - 1; I >= 0; I--) { 
        C = C * Base + A[I]; 
        R[I] = C / B; 
        C %= B; 
    } 
    R.Len = A.Len; 
    while (R.Len > 0 && R[R.Len - 1] == 0) R.Len--; 
    return C; 
} 

xnum operator/(const xnum& A, const xnum& B) { 
    int I; 
    xnum R, Carry = 0; 
    int Left, Right, Mid; 
    for (I = A.Len - 1; I >= 0; I--) { 
        Carry = Carry * Base + A[I]; 
        Left = 0; 
        Right = Base - 1; 
        while (Left < Right) { 
            Mid = (Left + Right + 1) / 2; 
            if (compare(B * Mid, Carry) <= 0) Left = Mid; 
            else Right = Mid - 1; 
        } 
        R[I] = Left; 
        Carry = Carry - B * Left; 
    } 
    R.Len = A.Len; 
    while (R.Len > 0 && R[R.Len - 1] == 0) R.Len--; 
    return R; 
} 
xnum operator%(const xnum& A, const xnum& B) { 
    int I; 
    xnum R, Carry = 0; 
    int Left, Right, Mid; 
    for (I = A.Len - 1; I >= 0; I--) { 
        Carry = Carry * Base + A[I]; 
        Left = 0; 
        Right = Base - 1; 
        while (Left < Right) { 
            Mid = (Left + Right + 1) / 2; 
            if (compare(B * Mid, Carry) <= 0) Left = Mid; 
            else Right = Mid - 1; 
        } 
        R[I] = Left; 
        Carry = Carry - B * Left; 
    } 
    R.Len = A.Len; 
    while (R.Len > 0 && R[R.Len - 1] == 0) R.Len--; 
    return Carry; 
} 

istream& operator>>(istream& In, xnum& V) { 
    char Ch; 
    for (V = 0; In >> Ch;) { 
        V = V * 10 + (Ch - '0'); 
        if (cin.peek() <= ' ') break; 
    } 
    return In; 
} 

ostream& operator<<(ostream& Out, const xnum& V) { 
    int I; 
    Out << (V.Len == 0 ? 0 : V[V.Len - 1]); 
    for (I = V.Len - 2; I >= 0; I--) for (int J = Base / 10; J > 0; J /= 10) Out << V[I] / J % 10; 
    return Out; 
} 

const int SCALE = 1001;
xnum a[SCALE];
int n;

xnum Gcd(const xnum &x, const xnum &y) {
	if (x % y == 0)
		return y;

	if (y % x == 0)
		return x;

	if (x < y) {
		return Gcd(y%x, x);
	} else {
		return Gcd(x%y, y);
	}
}

xnum FabsMinus(const xnum & x, const xnum & y) {
	if (x < y) {
		return y - x;
	} else {
		return x - y;
	}
}

vector<xnum> sub;
xnum Solve() {
	// xnum MI = FabsMinus(a[0],  a[1]);
	sub.resize(0);
	sub.reserve(SCALE * SCALE);
	for (int i = 0; i < n; ++i) {
		for (int j = i + 1; j < n; ++j) {
			xnum tmp = FabsMinus(a[i], a[j]);
			if (tmp == 0)
				continue;
			sub.push_back(tmp);
		}
	}
	if (sub.empty())
		return 0;

	xnum g = sub[0];
	for (int i = 0; i < sub.size(); ++i) {
		g = Gcd(g, sub[i]);
	}
	if (g == 1)
		return 0;

	if (a[0]%g == 0)
		return 0;
	return g - (a[0]%g);
}

int main() {
	//freopen("in.txt","r",stdin);
	freopen("B-large(2).in","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	while (cin >> t) {
		for (int i = 0; i < t; ++i) {
			cin >> n;
			for (int j = 0; j < n; ++j) {
				cin >> a[j];
			}
			/*
			for (int j = 0; j < n; ++j) {
				cout << a[j] << " ";
			}
			cout << endl;
			*/
			cout << "Case #" << i + 1 << ": ";
			xnum res = Solve();
			cout << res << endl;
		}
	}
}