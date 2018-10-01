def run(case_num):
    num_ingredients, num_packages_per_ingredient = [int(x) for x in input().strip().split()]
    one_serving = [int(x) for x in input().strip().split()]
    ingredient_quantities = [[int(x) for x in input().strip().split()] for _ in range(num_ingredients)]
    sizes_used = set()

    for serving_size, ingredient_quantity in zip(one_serving, ingredient_quantities):
        for package_num in range(len(ingredient_quantity)):
            servings = ingredient_quantity[package_num] / serving_size
            valid_servings = []

            check_serving_size = int(servings)
            while check_serving_size > 0 and (check_serving_size*0.9) <= servings <= (check_serving_size*1.1):
                valid_servings.append(check_serving_size)
                check_serving_size -= 1
            check_serving_size = int(servings) + 1
            while (check_serving_size * 0.9) <= servings <= (check_serving_size * 1.1):
                valid_servings.append(check_serving_size)
                check_serving_size += 1

            ingredient_quantity[package_num] = valid_servings
            sizes_used.update(valid_servings)

    total = 0

    # for ingredients in zip(*ingredient_quantities):
    #     possible = set(ingredients[0])
    #     for g in ingredients[1:]:
    #         possible.intersection_update(g)
    #     if len(possible) > 0:
    #         total += 1

    for size_used in sizes_used:
        while all(any(size_used in package for package in ingredient_quantity)
                  for ingredient_quantity in ingredient_quantities):
            total += 1
            for ingredient_quantity in ingredient_quantities:
                to_remove = None
                for package in ingredient_quantity:
                    if size_used in package:
                        if not to_remove or len(package) < len(to_remove):
                            to_remove = package
                ingredient_quantity.remove(to_remove)

    assert total <= num_packages_per_ingredient

    print("Case #{}: {}".format(case_num, total))

for case in range(int(input())):
    run(case+1)
