#include<fstream.h>
#include<conio.h>
#include<stdio.h>
#include<math.h>

void main()
{
	int A, B, n, m, d, T, S[50],i,temp,r,count;
	fstream fi,fo;
	fi.open("input.txt",ios::in);
	fo.open("output.txt",ios::out);

	fi>>T;
	//fi.getline(G[0],100,'\n');
	i=0;
	while(fi && i<T)
	{
		//fi.getline(G[i],102,'\n');
		fi>>A>>B;
		if(fi.eof())
			break;
		temp = A;
		d = 0;
		while(temp>0)
		{
			temp/=10;
			d++;

		}

		n = A-1;
		count = 0;
		while(n<B)
		{
			n++;
			r = d-1;
			if(n/pow(10,d-1) == 0)
				continue;
			while(r>0)
			{
				m = (n%(int)pow(10,r))*pow(10,d-r) + n/pow(10,r);
				if(m/pow(10,d-1) != 0)
					if(m>n && m<=B)
						count++;
				r--;

			}

		}

		S[i] = count;
		i++;

	}

	for(i=0 ; i<T ; i++)
		fo<<"\nCase #"<<(i+1)<<": "<<S[i];

	fo.close();
	fi.close();

}
