#include <iostream>

using namespace std;




long long x0, y0, x1, y1, x2, y2;
long long w, h;

void Load()
{
	cin >> w >> h;
	cin >> x1 >> y1;
	cin >> x2 >> y2;
	cin >> x0 >> y0;
}


int was[1100000];
int q[1100000];
int hd, tl;


int ma[101][101];

void Solve()
{

	long long clb, crb, lx, ly,  lb, rx, ry, rb;
	long long ans = 0;
	long long a, l , r, t;

	lx = 0 - x0;
	ly = 0 - y0;
	rx = w- 1 - x0;
	ry = h- 1 - y0;

	memset(ma, 0, sizeof(ma));
	ma[x0][y0] = 1;
	int ans1=0;
	int f = 1;
	while (f)
	{
		f= 0;
		int i, j;
		j = 0;
		for (i = 0; i < w; i++)
		{
			for (j = 0; j < h; j++)
			{
				if (ma[i][j] == 1) break;
			}
			if (ma[i][j] == 1) break;
		}

		if (ma[i][j] == 1)
		{
			f = 1;
			ans1++;
			ma[i][j] = 2;
			if (i+x1 >= 0 && i + x1 < w && j + y1 >= 0 && j + y1 < h)
			{
				if (ma[i+x1][j+y1] == 0) ma[i+x1][j+y1] = 1;
			}
			if (i+x2 >= 0 && i + x2 < w && j + y2 >= 0 && j + y2 < h)
			{
				if (ma[i+x2][j+y2] == 0) ma[i+x2][j+y2] = 1;
			}
		}

	}
/*
	if (x1*y2-x2*y1 == 0) 
	{
		memset(was, 0, sizeof(was));
		long long dx, dy;
		if (x1 != 0 || y1 != 0)
		{
			dx = x1;
			dy = y1;
		}
		else
		{
			dx = x2;
			dy = y2;
		}
		if (dx == 0 && dy == 0)
		{
			cout << "1\n";
			return;
		}
		long long d = __gcd(abs(dx), abs(dy));
		dx /= d;
		dy /= d;

		cerr << dx << ' ' << dy << "\n";

		for (l = -1000000; l < 0; l++)
			if (x0+dx*l >= 0 && y0 + dy*l >= 0 && x0+dx*l < w && y0+dy*l < h)
				break;

		for (r = 1000000; r > 0; r--)
			if (x0+dx*r >= 0 && y0 + dy*r >= 0 && x0+dx*r < w && y0+dy*r < h)
				break;

		long long d1, d2;
		if (dx != 0)
			d1 = x1 / dx;
		else
			d1 = y1 / dy;
		if (dx != 0)
			d2 = x2 / dx;
		else
			d2 = y2 / dy;

		cerr <<l << " " << r << " "  << d1 << " " << d2 << "\n";

		r = r - l;
		hd = tl = 0;
		q[0] = -l;
		was[0] = 1;



		while (hd <= tl)
		{
			d = q[hd++];
			ans++;
			if (d + d2 > 0 && d + d2 <= r & was[d+d2] == 0)
			{
				q[++tl] = d+d2;
				was[d+d2] = 1;
			}
			if (d + d1 > 0 && d + d1 <= r & was[d+d1] == 0)
			{
				q[++tl] = d+d1;
				was[d+d1] = 1;
			}


		}


		cout << ans << "\n";
		return;
	}
	//	cerr << lx << ' ' << rx << "  " << ly << ' ' << ry << "\n";


	for (a = 0; a <= 2000000; a++)
	{
		lb = 0;
		rb = 20000000;
		l = lx - a * x1;
		r = rx - a * x1;
//		cerr << x2 << "*b " << l << " " << r << "\n";
		if (x2 == 0)
		{
			if (l > 0 || r < 0)
			{
				clb = -1;
				crb = -2;
			}
			else
			{
				clb = -1;
				crb = 2000000;
			}
		}
		else
		{
			if (x2 < 0)
			{
				t = l; l = r; r = t;
				l = -l;
				r = -r;
			}
			clb = l /  abs(x2);
			while (clb * abs(x2) < l) clb++;
			crb = r / abs(x2);
			while (crb * abs(x2) > r) crb--;
		}

//		cerr << clb << ' ' << crb << "\n";

		if (clb > lb) lb = clb;
		if (crb < rb) rb = crb;

		l = ly - a * y1;
		r = ry - a * y1;

//		cerr << y2 << "*b " << l << " " << r << "\n";

		if (y2 == 0)
		{
			if (l > 0 || r < 0)
			{
				clb = -1;
				crb = -2;
			}
			else
			{
				clb = -1;
				crb = 2000000;
			}
		}
		else
		{
			if (y2 < 0)
			{
				t = l; l = r; r = t;
				l = -l;
				r = -r;
			}
			clb = l /  abs(y2);
			while (clb * abs(y2) < l) clb++;
			crb = r / abs(y2);
			while (crb * abs(y2) > r) crb--;
		}

//		cerr << clb << ' ' << crb << "\n";

		if (clb > lb) lb = clb;
		if (crb < rb) rb = crb;

		if (rb < lb) rb = lb - 1;

		ans += rb - lb + 1;	
	}
	if (ans1 != ans)
	{
		cerr << "Botva\n";
		cerr << ans1 << " " << ans<< "\n";
	}
    */
	cout << ans1 << "\n";

}


int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int nt, tt;
	cin >> nt;
	for (tt = 1; tt <= nt; tt++)
	{
		Load();
		cerr << tt << "\n";
		cout << "Case #" << tt << ": ";
		Solve();
	}
	return 0;
}
