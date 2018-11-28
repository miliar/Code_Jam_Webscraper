#include <iostream>
#include <vector>
#include <algorithm>

typedef	std::vector<int> candies;

int	read(candies &list)
{
	int nb;
	std::cin >> nb;

	list.resize(nb);
	for(int i = 0; i < nb; i++)
	{
		std::cin >> list[i];
	}

	return nb;
}

int sub_tree(int va, int vb, int sxora, int sxorb, int i, candies &list, int nb)
{
	if(i == nb)
	{
		if(sxora != sxorb || va == 0 || vb == 0)
			return -1;
		return (va > vb) ? va : vb;
	}

	
	//Left
	int vleft = -1;
	{
		const int cp_va = va + list[i];
		const int cp_sxora = sxora ^ list[i];
		vleft = sub_tree(cp_va, vb, cp_sxora, sxorb, i+1, list, nb);
	}

	//Right
	int vright = -1;
	{
		const int cp_vb = vb + list[i];
		const int cp_sxorb = sxorb ^ list[i];
		vright = sub_tree(va, cp_vb, sxora, cp_sxorb, i+1, list, nb);
	}
	return (vleft > vright) ? vleft : vright;
}

int	calc()
{
	//Load candies
	candies list;
	int nb = read(list);
	//We have nb >= 2!

	return sub_tree(0, 0, 0, 0, 0, list, nb);
}

int main(void)
{
	int nb_cases;

	//For each cases
	std::cin >> nb_cases;
	for(int i = 1; i <= nb_cases; i++)
	{

		int r = calc();

		if(r > 0)
			std::cout << "Case #" << i << ": " << r << "\n";
		else
			std::cout << "Case #" << i << ": NO\n";
	}
	return 0;
}
