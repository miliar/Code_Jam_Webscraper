T = int(input())
for t in range(1, T + 1):
    ANS = 0
    N, P = map(int, input().split(' '))
    recipes = list(map(int, input().split(' ')))
    kit_per_packages_item = list()
    for n in range(N):
        packages = list(map(int, input().split(' ')))
        kit_per_packages = list()
        for package in packages:
            recipe = recipes[n]
            kit_per_package = list()
            min_n_kit = int(package // (recipe * 1.1))
            max_n_kit = int(package // (recipe * 0.9))
            for n_kit in range(min_n_kit, max_n_kit + 2):
                if n_kit * recipe * 0.9 <= package <= n_kit * recipe * 1.1:
                    kit_per_package.append(n_kit)
            if len(kit_per_package) > 0:
                kit_per_packages.append(kit_per_package)
        kit_per_packages.sort()
        kit_per_packages_item.append(kit_per_packages)
    # print(kit_per_packages_item)

    for i_target_kit_per_package, target_kit_per_package in enumerate(kit_per_packages_item[0]):
        for target_kit in target_kit_per_package:
            i_package_each_item = [-1] * N
            i_package_each_item[0] = i_target_kit_per_package
            for i_item in range(1, N):
                for i_package in range(len(kit_per_packages_item[i_item])):
                    if target_kit in kit_per_packages_item[i_item][i_package]:
                        i_package_each_item[i_item] = i_package
                        break
            if -1 not in i_package_each_item:
                ANS += 1
                for i_item in range(1, N):
                    del(kit_per_packages_item[i_item][i_package_each_item[i_item]])
                break

    print('Case #{}: {}'.format(t, ANS))
