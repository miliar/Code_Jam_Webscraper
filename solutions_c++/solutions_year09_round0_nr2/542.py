#include <iostream>
#include <vector>

using namespace std;

typedef vector < vector <char> > Mat;

void paint (Mat *flow, int i, int j, int h, int w, char l) {

	if(i>0 && (*flow)[i-1][j] == 'S') {
		(*flow)[i-1][j] = l;
		paint(flow, i-1, j, h, w, l);
	}
	if(j>0 && (*flow)[i][j-1] == 'E') {
		(*flow)[i][j-1] = l;
		paint(flow, i, j-1, h, w, l);
	}
	if(i<h-1 && (*flow)[i+1][j] == 'N') {
		(*flow)[i+1][j] = l;
		paint(flow, i+1, j, h, w, l);
	}
	if(j<w-1 && (*flow)[i][j+1] == 'W') {
		(*flow)[i][j+1] = l;
		paint(flow, i, j+1, h, w, l);
	}

	return;
}

int main () {
	int h, w;
	int t, n;
	int i, j, d;
	int north, south, east, west;
	char l;
	vector < vector <int> > v;
	vector < vector <char> > flow;
	vector < vector <char> > f;
	vector <int> aux;
	vector <char> c;
	vector <char>::iterator k;

	cin >> n;

	for(t=1; t<=n; t++) {

		cin >> h >> w;
		v.clear();
		aux.clear();
		c.clear();
		flow.clear();
		f.clear();
		for(j=0; j<w; j++)
			c.push_back('#');
		for(i=0; i<h; i++)
			flow.push_back(c);

		for(i=0; i<h; i++) {
			aux.clear();
			for(j=0; j<w; j++) {
				cin >> d;
				aux.push_back(d);
			}
			v.push_back(aux);
		}

		// find sinks
		for(i=0; i<h; i++)
			for(j=0; j<w; j++) {
				if(i>0) north = v[i-1][j];
				else north = INT_MAX;
				if(j>0) west = v[i][j-1];
				else west = INT_MAX;
				if(i<h-1) south = v[i+1][j];
				else south = INT_MAX;
				if(j<w-1) east = v[i][j+1];
				else east = INT_MAX;

				if(north>=v[i][j] && west>=v[i][j] && south>=v[i][j] && east>=v[i][j])
					flow[i][j] = 'H';
				else if(north<=south && north<=west && north<=east)
					flow[i][j] = 'N';
				else if(west<=north && west<=south && west<=east)
					flow[i][j] = 'W';
				else if(east<=north && east<=south && east<=west)
					flow[i][j] = 'E';
				else if(south<=north && south<=west && south<=east)
					flow[i][j] = 'S';
				else
					flow[i][j] = 'N';
		}

		l = 'a';
		for(i=0; i<h; i++)
			for(j=0; j<w; j++)
				if(flow[i][j] == 'H') {
					flow[i][j] = l;
					paint(&flow, i, j, h, w, l);
					l++;
				}

		f = flow;
		l = 'a';
		c.clear();
		for(i=0; i<h; i++)
			for(j=0; j<w; j++) {
				k = find(c.begin(), c.end(), flow[i][j]); 
				if (k != c.end())
					f[i][j] = k-c.begin()+'a';
				else {
					c.push_back(flow[i][j]);
					f[i][j] = l;
					l++;
				}
					
			}

		cout << "Case #" << t << ":" << endl;
		for(i=0; i<h; i++) {
			for(j=0; j<w; j++)
				cout << f[i][j] << " ";
			cout << endl;
		}

	}

	return 0;
}