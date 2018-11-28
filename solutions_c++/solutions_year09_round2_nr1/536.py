#include <simple.h>

	// number of cases 100;  animals 100; features 100
	
	typedef std::set<string>    animal_t;


struct	value_t {
		value_t () : value(0.0), fiture(""), yes(0), no(0) {};
		double 		value;
		string		fiture;
		value_t*	yes;
		value_t*	no;

	double	eval(animal_t a) {
		double fit = value;	
		if (!fiture.empty()) {
			if (a.count(fiture)>0)	fit *=yes->eval(a);
			else      	     	fit *=no ->eval(a);
		}
		return fit;
	}

	void	print() {
		cerr << value << " " << fiture <<  endl;
		if (!fiture.empty()) {
			cerr << "\t";  yes->print();
			cerr << "\t";  no->print();
		}
	}
	void	read() {
		// (
		while(cin.get()!='('); 

		// value
		cin >> value ;
							//cerr << "value: " << value << endl;
		//while(c=cin.get(),  ispace(c)
		char c;
		cin >> c;
		if (c==')') return;

		// name
		cin.putback(c);
		cin >> fiture; 
							//cerr << "fiture: " << fiture << endl;

		yes = new value_t();	yes->read();
		no  = new value_t();	no->read();

		cin >> c;
		if (c==')') return;
							//cerr << "ERROR no closing ) " << endl;
		
	}

};


int main() {
	//char	line[1001];
	char	s[1001];
	int CS;
	cin  >> CS; cin.getline(s,1000); 


	for ( int cs=1;   cs<=CS ;   cs++)  {
		value_t	tree;

		cout << "Case #" << cs << ": \n";		

		int LN;
		cin  >> LN; cin.getline(s, 1000); 
								//cerr << "LN: " << LN << endl;
		tree.read();		cin.getline(s,1000);
		
		int AN, an_n_fitures;
		cin  >> AN; cin.getline(s,1000); 		
								//cerr << "AN: " << AN << endl;
		for (int an=1; an <=AN; an++) {
			animal_t    animal;
			string str;
			cin >> str >> an_n_fitures;  
			for (int ft=1;  ft <=an_n_fitures;  ft++) {
				cin >> str;
				animal.insert(str);
								//cerr << "ft: " << ft << str <<  endl;
			}
			cin.getline(s, 1000);
			//tree.print();
			cout << tree.eval(animal) << endl; 
		}
	}
										//cerr << endl;
	return 0;
}
