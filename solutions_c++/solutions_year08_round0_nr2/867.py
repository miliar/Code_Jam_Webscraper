/* ****************************************
	train.cpp - Greg Tourville - July 17th - Google Code Jam - Problem B
*/


#include <iostream>
#include <fstream>
#include <assert.h>

//using namespace std;


/* ****************************************
	CLinkedList - Doubly Linked List Implementation
*/

template <class T> class CLinkedList;

template <class T> class CListEntry
{
public:
	CListEntry();
	CListEntry( T* );
	~CListEntry();

	void Insert( T* data );
	void Remove();
	CListEntry<T>* GetNext();
	CListEntry<T>* GetPrev();

	T* data;

	CListEntry<T>* prev;
	CListEntry<T>* next;
	CLinkedList<T>* parent;
};

template <class T> class CLinkedList
{
public:
	CLinkedList();
	~CLinkedList();

	void Add( T* data );
	void Add( T* data, int index );
	void RemoveEntry( CListEntry<T>* l );
	CListEntry<T>* FindEntry( T* data );
	int GetLength();
	CListEntry<T>* GetFirst();
	CListEntry<T>* GetLast();

	int length;
	CListEntry<T>* first;
	CListEntry<T>* last;
};

#ifndef NULL
	#define NULL 0
#endif

template <class T>
CLinkedList<T>::CLinkedList()
{
	length = 0;
	first = NULL;
	last = NULL;
}

template <class T>
CLinkedList<T>::~CLinkedList()
{
	CListEntry<T>* l = first;
	while ( l )
	{
		RemoveEntry( l );
		l = first;
	}
}

template <class T>
void CLinkedList<T>::Add( T* data )
{
	if ( first && last )
	{
		last->next = new CListEntry<T>( data );
		last->next->prev = last;
		last = last->next;
		length++;
	} else {
		first = new CListEntry<T>( data );
		last = first;
		first->next = NULL;
		first->prev = NULL;
		length++;
	}
	
	last->parent = this;
}

template <class T>
void CLinkedList<T>::Add( T* data, int index )
{
	if ( index == 0 )
	{
		if ( first && last )
		{
			CListEntry<T>* newEntry = new CListEntry<T>( data );
			newEntry->prev = NULL;
			newEntry->next = first;
			newEntry->parent = this;
			first->prev = newEntry;
			first = newEntry;
		} else {
			CListEntry<T>* newEntry = new CListEntry<T>( data );
			newEntry->prev = NULL;
			newEntry->next = NULL;
			newEntry->parent = this;
			first = newEntry;
			last = newEntry;
		}
		length++;
	} else if ( index < length ) {
		CListEntry<T>* insertionPoint = GetFirst();

		for ( index--; index > 0; index-- )
			insertionPoint = insertionPoint->GetNext();

		insertionPoint->Insert( data );
	} else if ( index == length ) {
		Add( data );
	}
}


template <class T>
void CLinkedList<T>::RemoveEntry( CListEntry<T>* l )
{
	if ( l == first )
		first = l->next;
	if ( l == last )
		last = l->prev;
	delete l;
	length--;
}

template <class T>
CListEntry<T>* CLinkedList<T>::FindEntry( T* data )
{
	CListEntry<T>* e = GetFirst();
	
	while ( e && e->data != data )
	{
		e = e->GetNext();
	}

	return e;
}

template <class T>
int CLinkedList<T>::GetLength()
{
	return length;
}

template <class T>
CListEntry<T>* CLinkedList<T>::GetFirst()
{
	return first;
}

template <class T>
CListEntry<T>* CLinkedList<T>::GetLast()
{
	return last;
}

template <class T>
CListEntry<T>::CListEntry()
{
	data = NULL;
	prev = NULL;
	next = NULL;
}

template <class T>
CListEntry<T>::CListEntry( T* data )
{
	this->data = data;
	prev = NULL;
	next = NULL;
}

template <class T>
CListEntry<T>::~CListEntry()
{
	delete data;
	Remove();
}


template <class T>
void CListEntry<T>::Insert( T* data )
{
	CListEntry<T>* newEntry = new CListEntry<T>( data );
	newEntry->next = next;
	if ( next )
		next->prev = newEntry;
	newEntry->parent = parent;
	newEntry->prev = this;
	next = newEntry;
	parent->length++;
}


template <class T>
void CListEntry<T>::Remove()
{
	if ( prev )
		prev->next = next;
	if ( next )
		next->prev = prev;
}

template <class T>
CListEntry<T>* CListEntry<T>::GetNext()
{
	return next;
}

template <class T>
CListEntry<T>* CListEntry<T>::GetPrev()
{
	return prev;
}


/* ****************************************
	CTime - Time Object that stores minutes & seconds, allows for adding a number of minutes, and >= comparison
*/


class CTime
{
public:
	CTime(int hours, int minutes)
	{
		assert(minutes >= 0 && minutes < 60);
		assert(hours >= 0 && hours < 24);

		mHours = hours;
		mMinutes = minutes;
	}

	void Add(int minutes)
	{
		assert(minutes >= 0);

		mMinutes += minutes;
		while (mMinutes >= 60)
		{
			mMinutes -= 60;
			mHours++;
		}
	}

	bool IsAfter(CTime* other)	// (identical times are considered "after" each other)
	{
		return (mHours > other->GetHours() || (mHours == other->GetHours() && mMinutes >= other->GetMinutes()));
	}

	int GetHours() { return mHours; }
	int GetMinutes() { return mMinutes; }

private:
	int mHours;
	int mMinutes;
};

/* ****************************************
	Computes the number of needed trains starting at a station based on the arrival and departure times for the station
*/

int NeededTrainsStation(CLinkedList<CTime>* stationArrivals, CLinkedList<CTime>* stationDepartures, int turnAroundTime)
{
	int neededTrains = 0;

	// Account for turn around time
	CListEntry<CTime>* list = stationArrivals->GetFirst();
	while (list)
	{
		list->data->Add(turnAroundTime);
		list = list->GetNext();
	}

	// Iterate through all departures
	CListEntry<CTime>* leaving = stationDepartures->GetFirst();
	while (leaving)
	{
		neededTrains++;	// For each departure, that is one more needed train

		// For each departure, attempt to find a prepped train that has arrived before depart time. If there are multiple, find the latest
		CListEntry<CTime>* prepped = NULL;
		CListEntry<CTime>* preppedSearch = stationArrivals->GetFirst();
		while (preppedSearch)
		{
			if ( leaving->data->IsAfter(preppedSearch->data)	// Check if this train is prepped on time
				&& (prepped == NULL || preppedSearch->data->IsAfter(prepped->data)) )	// And see if it is later than the current best
			{
				prepped = preppedSearch;
			}

			preppedSearch = preppedSearch->GetNext();
		}

		// If we have found a prepped, arrived train, decrement the needed trains and remove it from the list of prepped candidates so it isn't used again
		if (prepped)
		{
			neededTrains--;
			stationArrivals->RemoveEntry(prepped);
		}


		leaving = leaving->GetNext();
	}

	return neededTrains;
}



// ****************************************************************************

int main(int argc, const char* argv[])	// Arguments to executed program should be 1) input file and 2) output file
{
	assert(argc == 3);

	std::ofstream output(argv[2]);
	std::ifstream input(argv[1], std::ifstream::in);

	assert(output.good());
	assert(input.good());
		

	// Process all cases
	int cases;
	input >> cases;
	for (int i = 1; i <= cases; i++)
	{
		CLinkedList<CTime>* arrivalsA = new CLinkedList<CTime>();
		CLinkedList<CTime>* arrivalsB = new CLinkedList<CTime>();
		CLinkedList<CTime>* departuresA = new CLinkedList<CTime>();
		CLinkedList<CTime>* departuresB = new CLinkedList<CTime>();

		int turnAroundTime;
		input >> turnAroundTime;

		int trainsA, trainsB;
		input >> trainsA >> trainsB;

		// Parse input for trains leaving A and arriving at B
		for (int j = 0; j < trainsA; j++)
		{
			int dHours, dMins;
			int aHours, aMins;
			char colon;

			input >> dHours >> colon >> dMins >> aHours >> colon >> aMins;

			arrivalsB->Add(new CTime(aHours, aMins));
			departuresA->Add(new CTime(dHours, dMins));
		}

		// Parse input for trains leaving B and arriving at A
		for (int j = 0; j < trainsB; j++)
		{
			int dHours, dMins;
			int aHours, aMins;
			char colon;

			input >> dHours >> colon >> dMins >> aHours >> colon >> aMins;

			arrivalsA->Add(new CTime(aHours, aMins));
			departuresB->Add(new CTime(dHours, dMins));
		}

		// Compute the answer and output it
		output << "Case #" << i << ": " << NeededTrainsStation(arrivalsA, departuresA, turnAroundTime) << ' '
			<< NeededTrainsStation(arrivalsB, departuresB, turnAroundTime) << std::endl;

		// Clean up
		delete arrivalsA;
		delete arrivalsB;
		delete departuresA;
		delete departuresB;
	}

	// Clean up
	input.close();
	output.close();

	return 0;
}


