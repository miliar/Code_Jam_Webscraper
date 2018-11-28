#include <stdio.h>
#include <string.h>
#include <fstream>
#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <utility>

using namespace std;

// deklaracia funkcii
bool compare_string();
int vypocitaj_pocet_switchov();
bool boli_uz_vsetky();
void nacitajData();

// deklaracia premennych
int searchEngines, queries, nCounter, counter, pocet_switchov;
int counterEngines, counterQueries;
string pomocna;
char slovo[100];
bool nulaKrokov = false;
bool viacKrokov = false;
bool pole_log_prvkov[100];

vector<string> engines;
vector<string> queries_v;

FILE *fp;
FILE *vystup;

/***
vypocita pocet, kolko switchov treba vykonat
***/
int vypocitaj_pocet_switchov()
{
	pocet_switchov = 0;
	bool boli_vsetky = false;
	// inicializujem prvky ci uz boli vsetky
	for(int g = 0; g < searchEngines; g++) 
	{
		pole_log_prvkov[g] = false;
	}
	for(int h = 0; h < queries; h++){

		/*** 
		porovnava prvky vyhladavacov a dotazov
		***/
		for(int j = 0; j < searchEngines; j++) 
		{
			// ak sa dotaz a vyhladavac rovnaju, tak prirad hodnotu bool danemu enginu a otestuj, ci uz vsetky nie su true
			if(queries_v[h].compare(engines[j]) == 0) 
			{
				// priradu logicku hodnotu vyhladavacu, ze uz je tam
				pole_log_prvkov[j] = true;
				// skontroluje sa, ci vsetky prvky nemaju hodnotu na true
				boli_vsetky = boli_uz_vsetky();
			}
			if(boli_vsetky) 
			{ 
				pocet_switchov++; 
//				cout <<"***///*** Uz boli vsetky, nastavuje SWITCH na dalsiu hodnotu..." << endl; 
				for(int g = 0; g < searchEngines; g++) 
				{
					pole_log_prvkov[g] = false;
				}
				pole_log_prvkov[j] = true;
				boli_vsetky = false;
//				cout << "***///*** Pocet switchov je: " << pocet_switchov << endl << endl;
				break; }
		}
	}
	

	// ak uz boli vsetky prvky, treba pripocitat k citacu krokov +1
	//boli_vsetky = boli_uz_vsetky();
	//if(boli_vsetky) cout << "Boli vsetky" << endl;
	//else cout << "Neboli vsetky" << endl;

	fprintf(vystup, "Case #%d: %d\n",counter, pocet_switchov); 
	return 0;
}

/***
zisti, ci boli uz vsetky prvky.
Ak ano, vrati true
***/
bool boli_uz_vsetky() 
{
	for(int g = 0; g < searchEngines; g++) 
	{
//		cout << "Prechadzanie searchEngines logicka hodnota cislo : " << searchEngines << " je: " << pole_log_prvkov[g] << endl;

	//	cout << "Pole log. prvkov cislo " << (g+1) << " je: " << pole_log_prvkov[g] << endl;
//ä		cout << "Hodnota " << engines[g].c_str() << " - " << pole_log_prvkov[g] << endl;
		// ak narazi na nejako false, tak vsetky este neboli. Vrati false
		if(pole_log_prvkov[g] == false) 
		{
//			cout << "Este vsetky neboli. Nastavujem... " << g << endl;
			return false;
		}
	}
	cout << endl;
	return true;
}

int main()
{

	fp = fopen("A-large.in", "r");
	vystup = fopen("A-large.out", "w");

	fscanf(fp,"%d",&nCounter);
	cout << "Pocet cases: " << nCounter << endl;

	//nCounter = 5;

	for (counter=1; counter<=nCounter; counter++)
	{
		nacitajData();
	}
	
	fclose(fp);
	fclose(vystup);
	int moja;
	cin >> moja;
	return 0;
}








/*** 
zisti, ci je potrebny vobec nejaky switch
ak nie, vypise case 0	
***/
bool compare_string() 
{

	for(int i = 0; i < searchEngines; i++)
	{
		nulaKrokov = false;

		for(int j=0; j < queries; j++)
		{
			if(engines[i].compare(queries_v[j]) == 0) 
			{ 
//				cout << "Compare string je nula, t.j. sa rovnaju" << endl;
				nulaKrokov = true; 
				break; 
			}
//			else { cout << "Nieje nula, nerovnaju sa!!!" << endl; nulaKrokov = false;}
		}
		if(nulaKrokov != true) 
		{ 
//			cout << "**** Neobsahuje rovnaku hodnotu" << endl; 
			return true;
			break; 
		}
	}
	if(nulaKrokov == true) return false;
}



void nacitajData()
{
	engines.clear();
	queries_v.clear();

	counterEngines = 0;
	counterQueries = 0;
	
	fscanf(fp, "%d", &searchEngines); // nacita pocet vyhl. strojov

	cout << "\n\nHlavny counter - SearchEngines = " << searchEngines << endl;

	fgets(slovo, 100, fp); // preskocenie medzery

	/**** Ulozi do vektora vyhl. stroje ****/
	for(counterEngines = 0; counterEngines < searchEngines; counterEngines++)
	{
		pomocna="";
		fgets(slovo, 100, fp); //(fp, "%s", slovo);
		pomocna.assign(slovo, strlen(slovo)-1);
		engines.push_back(pomocna);
	}
	/**** Vypise vyhl. stroje ****/
/*	for(counterEngines = 0; counterEngines < engines.size(); counterEngines++)
	{
		cout << "Vypis searchEngines: ";
		cout << engines[counterEngines].c_str() << endl;
	}
*/
	fscanf(fp, "%d", &queries); // nacita pocet dotazov

	cout << "Hlavny counter - Queries = " << queries << endl;
	
	fgets(slovo, 100, fp); // preskocenie medzery

	/**** Ulozi do vektora dotazy ****/
	for(counterQueries = 0; counterQueries < queries; counterQueries++)
	{
		pomocna = "";
		fgets(slovo, 100, fp); //(fp, "%s", slovo);
		pomocna.assign(slovo, strlen(slovo)-1);
		queries_v.push_back(pomocna);
	}

	/**** Vypise dotazy ****/
/*	for(counterQueries = 0; counterQueries < queries_v.size(); counterQueries++)
	{
		cout << "Vypis queries ";
		cout << queries_v[counterQueries].c_str() << endl;
	}
*/
	/*for(counterEngines; counterEngines < searchEngines; counterEngines++)
	{
		fscanf(fp, "%s", &engines[counterEngines]);

	}*/
	//fscanf(fp,"%d %d %d %d %d %d",&x1,&y1,&x2,&y2,&x3,&y3);
	//fprintf(vystup, "Case #%d: ",counter);
	//fputs("triangle\n", vystup);
	
	viacKrokov = compare_string();

	if(viacKrokov == true) 
	{ 
		fprintf(vystup, "Case #%d: %d\n",counter, 0); 
	}
	else 
	{
//		cout << "idem pocitat switche" << endl;
		vypocitaj_pocet_switchov();
		// pocet_switchov je v premennej pocet_switchov
	}

}
