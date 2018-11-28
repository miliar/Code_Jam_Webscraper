
#include <iostream>
#include <fstream>
#include <map>
#include <vector>
using namespace std;
using std::cout;

bool rs (pair<int,int> i, pair<int,int> j) { return (j.first < i.first); }

int main () 
{
    ifstream myfile;
	int datasets=0;
    myfile.open ("B-small-attempt6.in");
   
	myfile >> datasets;

	for (int i=0; i< datasets; i++) {	

		int sa=0;
		int sb=0;

		int x=0;
		myfile >> x;			

		map<int,int> depa;
		map<int,int> depb;
		vector<pair<int,int> > veca,vecb;

		int ta=0;
		int tb=0;
		myfile >> ta;
		myfile >> tb;
		
		pair<int,int> ea,eb;
		
		if (ta > 0 || tb > 0) {
			string t;
			for (int i=0; i< ta; i++) {
				myfile >> t;
								
	 		    char *cstr = new char [t.size()+1];
			    strcpy (cstr, t.c_str());				
				cstr[2]=cstr[3];
				cstr[3]=cstr[4];
				cstr[4]=cstr[5];
				int d = atoi(cstr);

				myfile >> t;
				
			    strcpy (cstr, t.c_str());				
				cstr[2]=cstr[3];
				cstr[3]=cstr[4];
				cstr[4]=cstr[5];
				int a = atoi(cstr);
				cstr[0]=0;
				cstr[1]=0;
				int m = atoi(cstr);
				delete[] cstr;

				int a2;
				if (m+x >= 60) a2=a+(x-(60-m))+100;
				else a2=a+x;

//cout << "a2:a" << a << " " << a2 << endl;

                depa.insert(pair<int,int>(d,a2));			

				veca.push_back(pair<int,int>(d,a2));
			}

			for (int i=0; i< tb; i++) {

				myfile >> t;
	 		    char *cstr = new char [t.size()+1];
			    strcpy (cstr, t.c_str());				
				cstr[2]=cstr[3];
				cstr[3]=cstr[4];
				cstr[4]=cstr[5];
				int d = atoi(cstr);


				myfile >> t;
			    strcpy (cstr, t.c_str());				
				cstr[2]=cstr[3];
				cstr[3]=cstr[4];
				cstr[4]=cstr[5];
				int a = atoi(cstr);
				cstr[0]=0;
				cstr[1]=0;
				int m = atoi(cstr);
				delete[] cstr;


				
				int a2;
				if (m+x >= 60) a2=a+(x-(60-m))+100;
				else a2=a+x;
//cout << "a2:a" << a << " " << a2 << endl;
//cout << a2 << endl;

                depb.insert(pair<int,int>(d,a2));			  
				 
				
				vecb.push_back(pair<int,int>(d,a2)); 
			}
		}

		if (veca.size() == 0 || vecb.size() == 0) {
			sa=veca.size();
			sb=vecb.size();
		}
			
		else {

		sort(veca.begin(),veca.end(),rs);
		sort(vecb.begin(),vecb.end(),rs);

		bool va=false;
		bool vb=false;
		int cd=0;

		// initial case, and subsequent cases
			
		while (veca.size() > 0 || vecb.size() > 0) {
///	cout << endl << " new set " << endl;
			if (veca.size() == 0) {
				sb += vecb.size();
				break;
				
			}
			if (vecb.size() == 0) {
				sa += veca.size();
				break;
			}

			ea = veca.back();
			eb = vecb.back();
			if (ea.second < eb.second) {
				sa++;
				//dont need map anymore - obfuscating,could be this second..
				cd=ea.second;											
//			cout << "veca " <<  veca.back().first << " " << veca.back().second << endl;
				veca.pop_back();
				vb=true;
				va=false;
			}
			else {
				sb++;
				cd=eb.second;
				//cd=depb.find(eb)->second;												
//			cout << "vecb " << vecb.back().first << " " << vecb.back().second << endl;
				vecb.pop_back();
				va=true;
				vb=false;
			}


			//fix case above, stick a loop around it for "new begs"
			
			bool found=false;
			do {
				//look for the departure in the appropriate vector			
				int rempos=0;
				found=false;

			 	if (vb) {
			        vector<pair<int,int> >::reverse_iterator it;
			       					 
					int i=0;
			        for (it = vecb.rbegin(); it != vecb.rend(); ++it,i++) {
	        	    	if ((*it).first >= cd) {
							rempos=i;							
							found=true;
							cd=(*it).first;
							break;
						}
							
					}
					
					if (found) {				
						cd=depb.find(cd)->second;										
//					cout << vecb.at(vecb.size()-(rempos+1)).first << " " << vecb.at(vecb.size()-(rempos+1)).second << endl;	
						vecb.erase(vecb.end()-(rempos+1));
	
					}
				
					va=true;
					vb=false;
				}

				else if (va) {
			        vector<pair<int,int> >::reverse_iterator it;
			        
					int i=0;
			        for (it = veca.rbegin(); it != veca.rend(); ++it,i++) {
	        	    	if ((*it).first >= cd) {
							rempos=i;							
							found=true;
							cd=(*it).first;
							break;
						}
							
					}
					
					if (found) {				
						cd=depa.find(cd)->second;											
//					cout << veca.at(veca.size()-(rempos+1)).first << " " << veca.at(veca.size()-(rempos+1)).second << endl;	
						veca.erase(veca.end()-(rempos+1));
					}
				
					vb=true;
					va=false;
				}

			} while (((veca.size() > 0 && va) || (vecb.size() > 0 && vb)) && found); 

		}

		}						
		
	    cout << "Case #" << i+1 << ": " << sa <<  " " << sb << endl;

	}

	

    myfile.close();
    return 0;
}


