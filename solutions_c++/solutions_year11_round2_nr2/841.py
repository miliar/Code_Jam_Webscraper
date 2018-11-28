#include <iostream>
#include <map>
#include <set>
#include <vector>
#include <queue>
#include <sstream>
#include <cmath>
#include <algorithm>

#define forp(a,b,i) for (int i = a; i < b; i++)
#define forn(a,b,j) for (int j = a; j >= b; j--)
#define pb push_back
#define mp make_pair

using namespace std;

int c,d;
vector<double> points;
vector<double> tp;
vector<double> moveD;

void moveBy(double m)	{
	int l,r;
	if (points.size() % 2 == 0)	{
		l = (points.size() / 2) - 1;
		r = (points.size() / 2);
	} else	{
		l = (points.size() / 2) - 1;
		r = (points.size() / 2) + 1;
	}
	
	// go left
	forn(l,0,i)	{
		tp[i] = points[i] - m;
	}
	// go right
	forp(r,points.size(),i)	{
		tp[i] = points[i] + m;
	}
	
	// merge
	if (abs(tp[l] - tp[r]) > d)	{
		double mid = tp[l] + (abs(tp[l] - tp[r]) / 2);
		tp[r] = mid + d/2;
		tp[l] = mid - d/2;
	}
	forp(1,points.size()-1,i)	{
		if (i <= l)	{
			if (abs(tp[i] - tp[i-1]) < d)
				tp[i] = tp[i-1] + d;
		} else	{
			if (abs(tp[i] - tp[i-1] > d))
				tp[i] = tp[i-1] + d;
		}
	}
// 	forn(l-1,0,i)	{
// 		if (abs(tp[i] - tp[i+1]) > d)	{
// 			tp[i] = tp[i+1] - d;
// 		}
// 	}
// 	forp(r+1, points.size(),i)	{
// 		if (abs(tp[i] - tp[i-1]) > d)	{
// 			tp[i] = tp[i-1] + d;
// 		}
// 	}
}

bool checkMove()	{
	
	cout << "check move : ";
	forp(0,points.size(),i)	{
		cout << tp[i] << " ";
	}
	cout << endl;
	cout << "check move : ";
	forp(0,points.size(),i)	{
		cout << points[i] << " ";
	}
	cout << endl;
	return (tp[points.size() -1] - tp[points.size() -2]) >= d;
	
	forp(0,points.size() - 1,i)	{
		if (abs(tp[i+1] - tp[i]) < d)	{
			return false;
		}
	}
	return true;
}

void solve(int z)	{

	double l = 0;
	double r = d+1;
	double m = (r-l) / 2;
	
// 	cout << l << " " << r << " " << abs(r-l)<< " " << (abs(r-l) < 0.000000001) <<  endl;
	
	while (abs(r-l) > 0.0000001)	{
		m = (r-l) / 2;
		m += l;
		cout << l << " " << r << " " << m << endl;
		moveBy(m);
		if (checkMove())	{
			r = m;
		} else	{
			l = m;
		}
	}
	
	cout << "Case #" << z << ": " << (((r-l) /2) + l) << endl;
}

double moveAt(int i)	{
	double cur = points[i];
	double maxr = 0;
	double maxl = 0;
	forp(i+1,points.size(),j)	{
		maxr = max((cur + d) - points[j], maxr);
		maxl = min((cur + d) - points[j], maxl);
		cur = cur + d;
	}
	cur = points[i];
	forn(i-1,0,j)	{
		maxr = max((cur - d) - points[j], maxr);
		maxl = min((cur - d) - points[j], maxl);
		cur = cur - d;
	}
// 	cout << i << " maxl " << maxl << " maxr " << maxr << endl;
	double maxf = abs(maxr + abs(maxl)) / 2;
// 	cout << maxf << endl;
	return maxf;
}

double moveAt2(int i)	{
	double maxr = 0;
	double maxl = 0;
	forp(1,i+1,j)	{
		if (tp[j] - tp[j-1] < d)	{
			forn(j,1,k)	{
				if (tp[k] - tp[k-1] < d)	{
					moveD[k-1] -= abs((tp[k] - d) - tp[k-1]);
					tp[k-1] = tp[k] - d;
				} else	{
					break;
				}
			}
		}
	}
	
	forn(tp.size() -2, i, j)	{
		if (tp[j] - tp[j+1] < d)	{
			forp(j,tp.size() -1,k)	{
				if (tp[k+1] - tp[k] < d)	{
					moveD[k+1] += abs((tp[k] + d) - tp[k+1]);
					tp[k+1] = tp[k] + d;
				} else	{
					break;
				}
			}
		}
	}
	
	forp(0,tp.size(),j)	{
		maxl = min(maxl, moveD[j]);
		maxr = max(maxr, moveD[j]);
	}
	
// 	cout << i << " check move : ";
// 	forp(0,points.size(),i)	{
// 		cout << points[i] << " ";
// 	}
// 	cout << "check move : ";
// 	forp(0,points.size(),i)	{
// 		cout << tp[i] << " ";
// 	}
// 	cout << endl;
// 	cout << maxl << " " << maxr << endl;
	return abs(maxr + abs(maxl)) / 2;
}

void solve2(int z)	{
	
	double minv = 1e50;
	forp(0,points.size(),i)	{
// 		cout << i << " " << minv << endl;
		forp(0,points.size(),j)	{
			tp[j] = points[j];
			moveD[j] = 0;
		}
		minv = min(minv,moveAt2(i));
	}
	cout << "Case #" << z << ": " << minv << endl;
}

int main()	{

	int t;
	cin >> t;
	forp(0,t,z)	{
		
		cin >> c >> d;
		points.clear();
		tp.clear();
		moveD.clear();
		
		forp(0,c,i)	{
			int v, p;
			cin >> p >> v;
			forp(0,v,j)	{
				points.pb(p);
				tp.pb(0);
				moveD.pb(0);
			}
		}
		
		solve2(z+1);
	}
}