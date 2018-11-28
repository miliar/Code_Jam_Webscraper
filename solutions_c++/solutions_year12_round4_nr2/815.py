#include<iostream>
#include<string.h>
#include<stdio.h>
#include<algorithm>
#include<set>
#include<cmath>
using namespace std;

float r[1005];
float x[1005];
float y[1005];
int n, w, h;

bool f(int i, int j)
{
	bool res = false;
	float dx = x[j] - x[i];
	float dy = y[j] - y[i];
	float dist2 = dx * dx + dy * dy;
	float dist = sqrt(dist2);
	float rs = r[i] + r[j] + 1;
	if(dist < rs){
		float s = (rs - dist) / dist / 2;
		dx *= s;
		dy *= s;
		x[i] -= dx;
		y[i] -= dy;
		x[j] += dx;
		y[j] += dy;
		res = true;
	}
	return res;
}

float constaint(int i)
{
	bool res = false;
	if(x[i] < 0) x[i] = 0, res = true;
	if(x[i] > w) x[i] = w, res = true;
	if(y[i] < 0) y[i] = 0, res = true;
	if(y[i] > h) y[i] = h, res = true;
	return res;
}

bool check()
{
	for(int i = 0; i < n; ++i){
		for(int j = i + 1; j < n; ++j){
			float dx = x[j] - x[i];
			float dy = y[j] - y[i];
			float dist2 = dx * dx + dy * dy;
			float k = (r[i] + r[j]) * (r[i] + r[j]);
			if(dist2 < k){
				cout << "error!" << endl;
				return false;
			}
		}
	}
	return true;
}

int main()
{
//	freopen("input.txt", "r", stdin);
//	freopen("output.txt", "w", stdout);

	int T;
	cin >> T;
	for(int cas = 1; cas <= T; ++cas){
		cin >> n >> w >> h;
		for(int i = 0; i < n; ++i){
			cin >> r[i];
			x[i] = ((float)rand() * w) / RAND_MAX;
			y[i] = ((float)rand() * h) / RAND_MAX;
		}
		bool collide = false;
		for(int step = 0; step < 1000; ++step){
			collide = false;
			for(int i = 0; i < n; ++i){
				for(int j = i + 1; j < n; ++j)
					collide = f(i, j) || collide;
			}
			for(int i = 0; i < n; ++i){
				collide = constaint(i) || collide;
			}
			if(!collide){
				break;
			}
		}
		printf("Case #%d:", cas);
		check();
		for(int i = 0; i < n; ++i){
			printf(" %.6f %.6f", x[i], y[i]);
		}
		printf("\n");
	}

	return 0;
}
