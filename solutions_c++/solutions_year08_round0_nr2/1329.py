#include <iostream>
#include <string>


using namespace std;

void selectionSort ( int* arr, int size )
{
   int indexOfMin;
   int pass;
   int j;

   for ( pass = 0; pass < size - 1; pass++ )
   {
           indexOfMin = pass;

           for ( j = pass + 1; j < size; j++ )
               if ( arr[j] < arr[indexOfMin] )
                   indexOfMin = j;

           swap ( arr[pass], arr[indexOfMin] );
   }
}

// swap function for integers
void swap ( int& x, int& y )
{
   int temp;
   temp = x;
   x = y;
   y = temp;
} 

int main () {

	int n;
	cin >> n;
	for (int i = 0; i < n; i++){
		int trainsA = 0;
		int trainsB = 0;
		int TurnAround = 0;		
		cin >> TurnAround;
		//cout << "here1" << endl;
		int na = 0;
		cin >> na;
		int nb = 0;
		cin >> nb;
		//cout << "here2" << endl;
		//Set up Arrays
		//cout << na << " "<< nb << endl;
		int* ADep = new int[na];
		//cout << "here1" << endl;
		int* AArr = new int[na];
		//cout << "here2" << endl;
		int* BDep = new int[nb];
		//cout << "here3" << endl;
		int* BArr = new int[nb];
		//cout << "here4" << endl;
		//Read in values
		
		for (int j = 0; j < na; j++){
			string time = "";
			cin >> time;
			//cout << time << endl;
			string hr = time.substr(0,2);
			int hrs = atoi(hr.c_str());
			string min = time.substr(3,2);
			int mins = atoi(min.c_str());
			ADep[j] = hrs * 60 + mins;
			//cout << "A Dep " << ADep[j] << endl;
			cin >> time;
			hr = time.substr(0,2);
			hrs = atoi(hr.c_str());
			min = time.substr(3,2);
			mins = atoi(min.c_str());
			AArr[j] = hrs * 60 + mins + TurnAround;
			//cout << "A Arr " << AArr[j] << endl;
		}
		
		for (int j = 0; j < nb; j++){
			string time = "";
			cin >> time;
			string hr = time.substr(0,2);
			int hrs = atoi(hr.c_str());
			string min = time.substr(3,2);
			int mins = atoi(min.c_str());
			BDep[j] = hrs * 60 + mins;
			//cout << "B Dep " << BDep[j] << endl;
			cin >> time;
			hr = time.substr(0,2);
			hrs = atoi(hr.c_str());
			min = time.substr(3,2);
			mins = atoi(min.c_str());
			BArr[j] = hrs * 60 + mins + TurnAround;
			//cout << "B Arr " << BArr[j] << endl;
		}  		
		
		//Calc trains needed at A
		//Sort A by departure		
		selectionSort(ADep,na);	
		//Sort B by arrival
		selectionSort(BArr, nb);				
		int otherCount = 0;
		for (int j = 0; j < na; j++)
		{
			//cout << "DEP "<<ADep[j] << " BTrain " << BArr[otherCount] << endl;
			if ((BArr[otherCount] >= 0) && (BArr[otherCount] <= ADep[j]))
			{
				BArr[otherCount] = -1;
				otherCount++;
				if (otherCount == nb)
					otherCount = 0;
			}
			else
				trainsA++;
		}
		
		//Sort B by departure
		selectionSort(BDep,nb);		
		//Sort A by arrival
		selectionSort(AArr, na);				
		otherCount = 0;
		for (int j = 0; j < nb; j++)
		{
			if ((AArr[otherCount] >= 0) && (AArr[otherCount] <= BDep[j]))
			{
				AArr[otherCount] = -1;
				otherCount++;
				if (otherCount == na)
					otherCount = 0;
			}
			else
				trainsB++;
		}
		delete [] ADep;
		delete [] AArr;
		delete [] BDep;
		delete [] BArr;
		ADep = NULL;
		AArr = NULL;
		BDep = NULL;
		BArr = NULL;
		cout << "Case #" << i + 1 << ": " << trainsA << " " << trainsB <<endl;
		//printf("WTF %i\n",i);
	}		
	return 0;
}
