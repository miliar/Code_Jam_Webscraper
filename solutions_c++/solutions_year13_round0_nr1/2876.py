#include <iostream>
#include <cstring>

using namespace std;

int main()
{
	int T, d, x, y;
	char table[5][5], current, final;
	bool won;

    cin >> T;

	for(int ix = 0; ix < T; ix++)
	{
		memset(table, '\0', sizeof(table));
        d = 0;
        final = 'z';

		for(int iy = 0; iy < 4; iy++)
		{
            won = true;

			for(int iz = 0; iz < 4; iz++)
			{   
				cin >> table[iy][iz];

				if(iz == 0)
		            current = table[iy][iz];
		        else if(current == 'T')
		    	    current = table[iy][iz];

                if((current != table[iy][iz] && table[iy][iz] != 'T') || table[iy][iz] == '.')
                	won = false;

				if(table[iy][iz] == '.')
			        d++;
			}

			if(won)
				final = current;
		}
     
        if(final != 'z')
        {	
        	cout << "Case #" << ix+1 << ": " << final << " won" << endl;
        	continue;
        }

        final = 'z';

		for(int iy = 0; iy < 4; iy++)
		{
            won = true;

			for(int iz = 0; iz < 4; iz++)
			{   
				if(iz == 0)
		            current = table[iz][iy];
		        else if(current == 'T')
		    	    current = table[iz][iy];

                if((current != table[iz][iy] && table[iz][iy] != 'T') || table[iz][iy] == '.')
                	won = false;
			}

			if(won)
				final = current;
		}
     
        if(final != 'z')
        {	
        	cout << "Case #" << ix+1 << ": " << final << " won" << endl;
        	continue;
        }

        final = 'z';
        won = true;

        for(int iy = 0; iy < 4; iy++)
        {
            if(iy == 0)
		        current = table[iy][iy];
		    else if(current == 'T')
		    	current = table[iy][iy];

            if((current != table[iy][iy] && table[iy][iy] != 'T') || table[iy][iy] == '.')
                won = false;
        }
        
        if(won)
        {	
        	cout << "Case #" << ix+1 << ": " << current << " won" << endl;
        	continue;
        }

        final = 'z';
        won = true;

        for(int iy = 0; iy < 4; iy++)
        {
            if(iy == 0)
		        current = table[iy][3-iy];
		    else if(current == 'T')
		    	current = table[iy][3-iy];

            if((current != table[iy][3-iy] && table[iy][3-iy] != 'T') || table[iy][3-iy] == '.')
                won = false;
        }
        
        if(won)
        {	
        	cout << "Case #" << ix+1 << ": " << current << " won" << endl;
        	continue;
        }

        if(d)
            cout << "Case #" << ix+1 << ": Game has not completed" << endl;
        else
        	cout << "Case #" << ix+1 << ": Draw" << endl;

	}

	return 0;
}