/*
 * Author: momodi
 * Created Time:  2010/5/8 21:54:14
 * File Name: b.cpp
 */
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
using namespace std;
#define out(v) cerr << #v << ": " << (v) << endl
#define SZ(v) ((int)(v).size())
const int maxint = -1u>>1;
template <class T> bool get_max(T& a, const T &b) {return b > a? a = b, 1: 0;}
template <class T> bool get_min(T& a, const T &b) {return b < a? a = b, 1: 0;}
const int base = 10000; 
const int cap = 200;
struct xnum { 
    int len; 
    int data[cap]; 
    xnum() : len(0) {} 
    xnum(const xnum& v) : len(v.len) { memcpy(data, v.data, len * sizeof *data); } 
    xnum(int v) : len(0) { for (; v > 0; v /= base) data[len++] = v % base; } 
    xnum& operator=(const xnum& v) { len = v.len; memcpy(data, v.data, len * sizeof *data); return *this; } 
    int& operator[](int index) { return data[index]; } 
    int operator[](int index) const { return data[index]; } 
}; 
int compare(const xnum& a, const xnum& b) { 
    int i; 
    if (a.len != b.len) return a.len > b.len ? 1 : -1; 
    for (i = a.len - 1; i >= 0 && a[i] == b[i]; i--); 
    if (i < 0) return 0; 
    return a[i] > b[i] ? 1 : -1; 
} 
xnum operator+(const xnum& a, const xnum& b) { 
    xnum r; 
    int i, c = 0; 
    for (i = 0; i < a.len || i < b.len || c > 0; i++) { 
        if (i < a.len) c += a[i]; 
        if (i < b.len) c += b[i]; 
        r[i] = c % base; 
        c /= base; 
    } 
    r.len = i; 
    return r; 
} 
xnum operator-(const xnum& a, const xnum& b) { 
    xnum r; 
    int c = 0; 
    r.len = a.len; 
    for (int i = 0; i < r.len; i++) { 
        r[i] = a[i] - c; 
        if (i < b.len) r[i] -= b[i]; 
        if (r[i] < 0) c = 1, r[i] += base; 
        else c = 0; 
    } 
    while (r.len > 0 && r[r.len - 1] == 0) r.len--; 
    return r; 
}
xnum operator*(const xnum& a, const int b) { 
    int i;
    if (b == 0) return 0;
    xnum r;
    int c = 0;
    for (i = 0; i < a.len || c > 0; i++) { 
        if (i < a.len) c += a[i] * b;
        r[i] = c % base;
        c /= base;
    } 
    r.len = i; 
    return r; 
} 
xnum operator*(const xnum& a, const xnum& b) {
    if (b.len == 0) return 0; 
    xnum r; 
    for (int i = 0; i < a.len; i++) { 
        int c = 0; 
        for (int j = 0; j < b.len || c > 0; j++) { 
            if (j < b.len) c += a[i] * b[j]; 
            if (i + j < r.len) c += r[i + j]; 
            if (i + j >= r.len) r[r.len++] = c % base;
            else r[i + j] = c % base;
            c /= base;
        }
    }
    return r; 
} 
xnum operator/(const xnum& a, const int b) { 
    xnum r; 
    int c = 0; 
    for (int i = a.len - 1; i >= 0; i--) { 
        c = c * base + a[i]; 
        r[i] = c / b; 
        c %= b; 
    } 
    r.len = a.len; 
    while (r.len > 0 && r[r.len - 1] == 0) r.len--; 
    return r; 
} 
xnum operator/(const xnum& a, const xnum& b) 
{ 
    xnum r, c = 0; 
    int left, right, mid; 
    for (int i = a.len - 1; i >= 0; i--) { 
        c = c * base + a[i]; 
        left = 0; 
        right = base - 1; 
        while (left < right) { 
            mid = (left + right + 1) / 2; 
            if (compare(b * mid, c) <= 0) left = mid; 
            else right = mid - 1; 
        } 
        r[i] = left; 
        c = c - b * left; 
    } 
    r.len = a.len; 
    while (r.len > 0 && r[r.len - 1] == 0) r.len--; 
    return r; 
} 
xnum operator%(const xnum& a, const xnum& b) { 
    xnum r, c = 0; 
    int left, right, mid; 
    for (int i = a.len - 1; i >= 0; i--) { 
        c = c * base + a[i]; 
        left = 0; 
        right = base - 1; 
        while (left < right) { 
            mid = (left + right + 1) / 2; 
            if (compare(b * mid, c) <= 0) left = mid; 
            else right = mid - 1; 
        } 
        r[i] = left; 
        c = c - b * left; 
    } 
    r.len = a.len; 
    while (r.len > 0 && r[r.len - 1] == 0) r.len--; 
    return c; 
} 
istream& operator>>(istream& in, xnum& v) { 
    char ch; 
    for (v = 0; in >> ch;) { 
        v = v * 10 + (ch - '0'); 
        if (cin.peek() <= ' ') break; 
    } 
    return in; 
} 
ostream& operator<<(ostream& out, const xnum& v) {
    out << (v.len == 0 ? 0 : v[v.len - 1]); 
    for (int i = v.len - 2; i >= 0; i--) for (int j = base / 10; j > 0; j /= 10) out << v[i] / j % 10; 
    return out; 
}
xnum gcd(xnum a, xnum b) {
    if (compare(b, xnum(0)) == 0) {
        return a;
    }
    return gcd(b, a % b);
}
int n;
xnum dt[1010];

int main() {
    int ca;
    scanf("%d", &ca);
    for (int cc = 1; cc <= ca; ++cc) {
        printf("Case #%d: ", cc);
        scanf("%d", &n);
        xnum mmin;
        for (int i = 0; i < n; ++i) {
            cin >> dt[i];
            if (i == 0) {
                mmin = dt[i];
            } else if (compare(dt[i], mmin) < 0) {
                mmin = dt[i];
            }
        }
        xnum ans = 0;
        for (int i = 0; i < n; ++i) {
            ans = gcd(ans, dt[i] - mmin);
        }
        cout << (ans - mmin % ans) % ans << endl;
    }
    return 0;
}

