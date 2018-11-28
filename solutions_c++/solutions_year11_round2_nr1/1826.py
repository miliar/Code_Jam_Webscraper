#include <iostream>
#include <fstream>

using namespace std;

const int maxn = 105;
int T, N;
double wp[maxn], owp[maxn], oowp[maxn];
char data[maxn][maxn];

void Test(double *a) {
    for (int i=0; i<N; ++i)
	cout << a[i] << " ";
    cout << endl;
}

double GetOwp(int i, int j) {
    double count = 0, sum = 0;
    for (int k=0; k<N; ++k) {
	if (k == i) continue;
	if (data[j][k] != '.')
	    sum++;
	if (data[j][k] == '1')
	    count++;
    }
    return count / sum;
}

void Proc() {
    double count = 0, sum = 0;
    for (int i=0; i<N; ++i) {
	wp[i] = 0;
	count = sum = 0;
	for (int j=0; j<N; ++j) {
	    if (data[i][j] != '.')
		sum++;
	    if (data[i][j] == '1')
		count++;
	}
	wp[i] = count / sum;
    }
    for (int i=0; i<N; ++i) {
	owp[i] = 0;
	count = 0;
	for (int j=0; j<N; ++j) {
	    if (data[i][j] != '.') {
		count++;
		owp[i] += GetOwp(i, j);
	    }
	}
	if (count) owp[i] /= count;
    }
    for (int i=0; i<N; ++i) {
	oowp[i] = 0;
	count = 0;
	for (int j=0; j<N; ++j) {
	    if (data[i][j] != '.') {
		count++;
		oowp[i] += owp[j];
	    }
	}
	if (count) oowp[i] /= count;
    }
}

void Output(int i) {
    cout << "Case #" << i+1 << ":\n";
    for (int i=0; i<N; ++i) {
	cout << 0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i] << endl;
    }
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("a.out", "w", stdout);

    cin >> T;
    for (int m=0; m<T; ++m) {
	cin >> N;
	for (int i=0; i<N; ++i)
	    for (int j=0; j<N; ++j)
		cin >> data[i][j];
	Proc();
	Output(m);
    }

    return 0;
}
