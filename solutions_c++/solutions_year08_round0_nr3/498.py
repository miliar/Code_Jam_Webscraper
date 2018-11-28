#ifndef __IOSTREAM__ 
#define __IOSTREAM__
#include <iostream>
#include <fstream>
#include <Vector>
#include <math.h>
#endif

using namespace std;

#define FILENAME  "C-small-attempt0.in"
#define GEN2 pow(2,0.5)
#define PI 3.1415926535857

void remove( vector<bool>* temp, int n) {
	for ( int i=n; i<(*temp).size()-1; i++ ) {
		(*temp)[i-1]=(*temp)[i];
	}
	(*temp).pop_back();
}

void main(){

	int n,i,j,k;
	float f, R, t, r, g;
	float result;
	float tempA,tempB;
	FILE *fp;

	ifstream file(FILENAME,ios::in);
	if(file.fail()){
		file.close();
		system("pause");
		exit(0);
	} 
	fp = fopen("output.txt", "w+");


	file>>n;

	for ( int casenum = 0; casenum < n; casenum++ ) {
		file>>f;
		file>>R;
		file>>t;
		file>>r;
		file>>g;

		result=0;
		if ( f >= g/2 ) {
			result = 0;
		} else if ( GEN2*r+GEN2*f+f >= R-t ) {
			result = 0;
		} else if ( g+r >=R-t ) {
			tempA=4*(PI/4-asin((f+r)/(R-t-f)))/(PI)*(R-t-f)*(R-t-f)/(R*R);
			tempB=4*(pow((R-t-f)*(R-t-f)-(r+f)*(r+f),0.5)-r-f)*(f+r)/(PI*R*R);
			result=tempA-tempB;
		} else {
			ldiv_t lx;
			double nn=floor((R-t)/(GEN2*g+2*GEN2*r));
			//double len = pow((R-t)*(R-t)-((g+2*r)*nn+r)*((g+2*r)*nn+r),0.5)-nn*(g+2*r)-r;

			double a,b,add,mianji=0;
			double count=nn*nn*4;
			double num=nn;
			double len = (R-t)-nn*(GEN2*g+2*GEN2*r)-GEN2*r;
			if ( len > GEN2*f+f ) {

				a = pow((R-t-f)*(R-t-f)-(num*(g+2*r)+r+f)*(num*(g+2*r)+r+f),0.5);

				if ( a>(num+1)*(g+2*r)-r-f ) {

					if ( a>(num+1)*(g+2*r)+r+f ) {
						b = (num+1)*(g+2*r)+r+f;
						mianji += ((R-t-f)*(R-t-f)*0.5*(asin(a/(R-t-f))+a/(R-t-f)*pow(1-a*a/((R-t-f)*(R-t-f)),0.5)) -
							(R-t-f)*(R-t-f)*0.5*(asin(b/(R-t-f))+b/(R-t-f)*pow(1-b*b/((R-t-f)*(R-t-f)),0.5))-
							(num)*(a-b)*(g+2*r)-(a-b)*(r+f))*8;
					}

					a = (num+1)*(g+2*r)-r-f;
					b=pow((R-t-f)*(R-t-f)-((num+1)*(g+2*r)-r-f)*((num+1)*(g+2*r)-r-f),0.5);
					mianji += ((R-t-f)*(R-t-f)*0.5*(asin(a/(R-t-f))+a/(R-t-f)*pow(1-a*a/((R-t-f)*(R-t-f)),0.5)) -
						(R-t-f)*(R-t-f)*0.5*(asin(b/(R-t-f))+b/(R-t-f)*pow(1-b*b/((R-t-f)*(R-t-f)),0.5))-
						num*(a-b)*(g+2*r)-(a-b)*(r+f))*4;
					mianji += (g-f-f)*(b-(num*(g+2*r)+r+f))*4;
					
				} else {
					b=num*(g+2*r)+r+f;
					mianji += ((R-t-f)*(R-t-f)*0.5*(asin(a/(R-t-f))+a/(R-t-f)*pow(1-a*a/((R-t-f)*(R-t-f)),0.5)) -
						(R-t-f)*(R-t-f)*0.5*(asin(b/(R-t-f))+b/(R-t-f)*pow(1-b*b/((R-t-f)*(R-t-f)),0.5))-
						num*(a-b)*(g+2*r)-(a-b)*(r+f))*4;
				}
			}

			for( int i=0; i<nn; i++ ) {

				add = floor(pow((R-t)*(R-t)-(g+2*r)*(nn-i)*(g+2*r)*(nn-i),0.5)/(g+2*r));
				count=count+(add-num)*(nn-i)*8;
				num = add;

				len = pow((R-t-f)*(R-t-f)-((nn-i-1)*(g+2*r)+r+f)*((nn-i-1)*(g+2*r)+r+f),0.5);
				if ( len > (num+1)*(g+2*r)-r-f ) {

					if ( len>(num+1)*(g+2*r)+r+f ) {
						a = pow((R-t-f)*(R-t-f)-((num+1)*(g+2*r)+r+f)*((num+1)*(g+2*r)+r+f),0.5);
						b = (nn-i-1)*(g+2*r)+r+f;
						mianji += ((R-t-f)*(R-t-f)*0.5*(asin(a/(R-t-f))+a/(R-t-f)*pow(1-a*a/((R-t-f)*(R-t-f)),0.5)) -
							(R-t-f)*(R-t-f)*0.5*(asin(b/(R-t-f))+b/(R-t-f)*pow(1-b*b/((R-t-f)*(R-t-f)),0.5))-
							(num+1)*(a-b)*(g+2*r)-(a-b)*(r+f))*8;
					}

					a = (nn-i)*(g+2*r)-r-f;
					b = pow((R-t-f)*(R-t-f)-((num+1)*(g+2*r)-r-f)*((num+1)*(g+2*r)-r-f),0.5);
					cout<<a<<"  "<<b<<endl;
					mianji += ((R-t-f)*(R-t-f)*0.5*(asin(a/(R-t-f))+a/(R-t-f)*pow(1-a*a/((R-t-f)*(R-t-f)),0.5)) -
						(R-t-f)*(R-t-f)*0.5*(asin(b/(R-t-f))+b/(R-t-f)*pow(1-b*b/((R-t-f)*(R-t-f)),0.5))-
						num*(a-b)*(g+2*r)-(a-b)*(r+f))*8;
					mianji += (g-f-f)*(b-((nn-i-1)*(g+2*r)+r+f))*8;

				} else if ( len > (num)*(g+2*r)+r+f ) {
					a = pow((R-t-f)*(R-t-f)-((num)*(g+2*r)+r+f)*((num)*(g+2*r)+r+f),0.5);
					if ( a>=(nn-i)*(g+2*r)-r-f ) a=(nn-i)*(g+2*r)-r-f;
					b = (nn-i-1)*(g+2*r)+r+f;
					cout<<a<<"  "<<b<<endl;
					mianji += ((R-t-f)*(R-t-f)*0.5*(asin(a/(R-t-f))+a/(R-t-f)*pow(1-a*a/((R-t-f)*(R-t-f)),0.5)) -
						(R-t-f)*(R-t-f)*0.5*(asin(b/(R-t-f))+b/(R-t-f)*pow(1-b*b/((R-t-f)*(R-t-f)),0.5))-
						num*(a-b)*(g+2*r)-(a-b)*(r+f))*8;

				}

			}
			mianji += count*(g-f-f)*(g-f-f);
			result = mianji/(PI*R*R);

		}
		
		fprintf(fp, "Case #%d: %f\n",casenum+1,1-result);

	}

	fclose(fp);
	file.close();
}
